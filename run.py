__author__ = 'kalko'

import sys, json
from pprint import pprint
from worksnaps import Worksnaps


class Run:
    __config = ''
    __from_date = '07/01/2016'
    __to_date = '07/31/2016'
    __report = []

    def __init__(self):
        self.init_config()

    def init_config(self):
        with open('config.json') as data_file:
             self.__config = json.load(data_file)
        return self.__config

    def get_config(self, type):
        return self.__config[type]

    def decode_report(self,ws_report):
        """
        row[0] = Project
        row[1] = User
        row[2] = Task
        row[3] = Date
        row[4] = Type
        row[5] = Activity Index (%)
        row[6] = Time Logged (hrs)
        """
        projects = self.get_config('projects')
        user_name = self.get_config('userName')
        projects_list = projects.keys()

        for row in ws_report:
            if(len(row)>2 and row[0] in projects_list and row[1] == user_name):
                self.__report.append({
                    "Project": row[0],
                    "User": row[1],
                    "Task": row[2],
                    "Date": row[3],
                    "Time": row[6],
                })
                print(row)
        print(self.__report)
        return ''







app = Run()

ws_config = app.get_config('worksnaps')

ws = Worksnaps(login=ws_config['login'], password=ws_config['password'])
from_date = '07/01/2016'
to_date = '07/31/2016'
ws_report = ws.get_report(from_date=from_date, to_date=to_date)
report = app.decode_report(ws_report)
# print(ws_report)
