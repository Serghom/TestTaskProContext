class Data:
    def __init__(self, value, nominal, date):
        self.value = value
        self.nominal = nominal
        self.date = date


class Valute:
    def __init__(self, json):
        self.id = json["ID"]
        self.num_code = json["NumCode"]
        self.char_code = json["CharCode"]
        self.name = json["Name"]

        self.values = []
        self.id_max = 0
        self.id_min = 0
        self.mid = 0


    def get_info(self):
        info = "Name:     {}\n"\
               "ID:       {}\n"\
               "NumCode:  {}\n"\
               "CharCode: {}".format(self.name, self.id, self.num_code, self.char_code)
        return info


    def get_status(self):
        status = "Максимальное значение:     {}₽ Дата:  {}\n"\
               "Минимальное значение:      {}₽ Дата:  {}\n"\
               "Среднее значение:          {}₽ \n"\
               "Номинал: {}".format(round(self.values[self.id_max].value, 2), self.values[self.id_max].date,
                                    round(self.values[self.id_min].value, 2), self.values[self.id_min].date,
                                    round(self.mid, 2), self.values[self.id_max].nominal)

        return status


    def set_values(self, list_data):
        self.values = list_data


    def find_max(self):
        for i, data in enumerate(self.values):
            if self.values[self.id_max].value < data.value:
                self.id_max = i
        # print(self.id_max, self.values[self.id_max].value)


    def find_min(self):
        for i, data in enumerate(self.values):
            if self.values[self.id_min].value > data.value:
                self.id_min = i
        # print(self.id_min, self.values[self.id_min].value)


    def find_mid(self):
        val = 0
        for data in self.values:
            val += data.value
        self.mid = val/len(self.values)