from fastapi import APIRouter, Path, Query
from converter import async_converter2, sync_converter, async_converter
from asyncio import gather
from schemas import ConverterInput, ConverterOutput

router = APIRouter()
# router = APIRouter(prefix="/converter") # ~~>substitui o /convertes
#API KEY: E2YGEC2AREG3LQ87

# Query parameter /url?to_currency=BRL,CND&price=4.32
# Path parameter
@router.get("/converter/{from_currency}")
def converter(from_currency: str
              , to_currency: str
              , price:float):
    to_currency = to_currency.split(",")

    result = []

    for currency in to_currency:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result.append(response)

    return result

@router.get("/converter/async/{from_currency}")
async def async_converter_router(from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$")
                                 , to_currency: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$")
                                 , price:float = Query(gt=0)
                                 ):
    to_currency = to_currency.split(",")

    courotine_list = []

    for currency in to_currency:
        corotine = async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        courotine_list.append(corotine)

    result = await gather(*courotine_list)
    return result

@router.get("/converter/async/v2/{from_currency}", response_model=ConverterOutput)
async def async_converter_router(
                                body: ConverterInput, 
                                from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$")                                
                                 ):
    to_currency = body.to_currency
    price = body.price

    courotine_list = []

    for currency in to_currency:
        corotine = async_converter2(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        courotine_list.append(corotine)

    result = await gather(*courotine_list)
    
    
    return ConverterOutput(
        message="Tudo certo",
        data=result
    )
