
from utils import refactor_date, mask_card, format_data
import pytest


@pytest.mark.parametrize('str_date, corr_date', [('2019-02-27T03:59:25.921176', '27.02.2019'),
                                                 ('2020-05-06T00:17:42.736209', '06.05.2020'),
                                                 ('2021-07-25T00:17:42.736209', '25.07.2021'),
                                                 ('2018-05-10T00:17:42.736209', '10.05.2018'),
                                                 ('2020-05-15T00:17:42.736209', '15.05.2020')])
def test_ref_date(str_date, corr_date):
    assert refactor_date(str_date) == corr_date


@pytest.mark.parametrize('str_card, mask', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                            ('Счет 35383033474447895560', 'Счет **5560'),
                                            ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                            ('MasterCard 3152479541115065', 'MasterCard 3152 47** **** 5065')])
def test_mask_card(str_card, mask):
    assert mask_card(str_card) == mask


def test_format_data():
    data = {
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {
          "amount": "96995.73",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967"
     }
    result = '14.04.2018 Перевод организации\nСчет **8655 -> Счет **8967\n96995.73 руб.'

    assert format_data(data) == result


