import requests
import subprocess
# import gui as g
import valute as v
import xml.etree.ElementTree as ET
from datetime import date, timedelta


def get_dates():
    cur = date.today() - timedelta(days=90)
    return cur.strftime('%d/%m/%Y') , date.today().strftime('%d/%m/%Y')


def create_requsts(date1, date2, rq):
    return r"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ={}".format(date1, date2, rq)


def create_valute_date(req):
    data_list = []
    xml = ET.fromstring(requests.get(req).text)
    for type_tag in xml.findall('Record'):
        value = float(type_tag.find('Value').text.replace(",", "."))
        nominal = int(type_tag.find('Nominal').text)
        date = type_tag.attrib['Date']
        data_list.append(v.Data(value, nominal, date))
    return data_list


def get_courses(val):
    date1, date2 = get_dates()
    data_list = create_valute_date(create_requsts(date1, date2, val.id))
    val.set_values(data_list)


def get_data_cbr():
    return requests.get(r'https://www.cbr-xml-daily.ru/daily_json.js').json()


def create_valutes():
    valutes_list = []
    valute_data = get_data_cbr()
    for CharCode in valute_data["Valute"]:
        valutes_list.append(v.Valute(valute_data["Valute"][CharCode]))

    return valutes_list


def find_max_min_mid(val):
    val.find_max()
    val.find_min()
    val.find_mid()



def output_console(valutes_list):
    valutes = ["{} | {}".format(valute.char_code, valute.name) for valute in valutes_list]
    done = True
    while done:
        for i, valute in enumerate(valutes):
            print("{} {}".format(i, valute))
        print('Введите номер валюты или введите "x" что бы завершить программу')
        answer = input(">> ")
        if answer.isdigit():
            if int(answer) > len(valutes) -1:
                print("Невозможное значение")
            else:
                get_courses(valutes_list[int(answer)])
                find_max_min_mid(valutes_list[int(answer)])
                print("{}\n\n{}".format(valutes_list[int(answer)].get_info(), valutes_list[int(answer)].get_status()))
                input("Введите любой символ для продолжения ")

        elif answer.lower() == "x":
            print("Выход")
            done = False

        else:
            print("Неизвестное значение")


if __name__ == '__main__':
    internet = False
    while not internet:
        try:
            subprocess.check_call(["ping", "-c 1", "www.google.ru"])
            print("Internet is up!")
            internet = True
        except subprocess.CalledProcessError:
            print("Internet is still down :(")
            exit(1)

    if internet:
        valutes_list = create_valutes()

        output_console(valutes_list)

        # g.Gui(valutes_list)