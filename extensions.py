from config import keys
import requests
import json


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(base: str, quote: str, amount: str) -> str:
        if int(amount) < 0:
            raise APIException("Вы не можете конвертировать отрицательное количество валюты")
        if base == quote:
            raise APIException("Вы не можете конвертировать валюту саму в себя")
        if base not in keys or quote not in keys:
            raise APIException("Была получена неправильная валюта")

        r = requests.get(f"https://v6.exchangerate-api.com/v6/eca033f5b059c17ece4b0fe9/latest/{keys[base]}")
        r = json.loads(r.content)
        text = f"{amount} {base} в {quote} = {float(r["conversion_rates"][keys[quote]]) * float(amount)}"

        return text
