__author__ = 'kalko'
from grab import Grab
import logging, csv
logging.basicConfig(level=logging.DEBUG)
class Worksnaps:
    g = Grab()
    __report_file = 'tmp/worksnaps/report.csv'

    def __init__(self, login, password):
        return
        self.g.setup(post={
            'login': login,
            'password': password,
            'btlogin':'Log In',
            'redir_url':'',
            'user_date':'',
            'source':'web',
            'invitation':''
                      })
        self.g.go('https://www.worksnaps.com/app/login.cgi')
        self.g.go('https://www.worksnaps.com/app/overview.cgi')

    def get_report(self, from_date, to_date):
        return self.read_report()
        self.g.setup(post={
            "timezone_offset": "3",
            "summarize_option": "0",
            "currency": "$",
            "currency_custom": "",
            "groupby_1": "project",
            "groupby_2": "user",
            "starttime": "",
            "endtime": "",
            "online_offline": "all",
            "task_name": "",
            "view": "dynamic",
            "op_code": "new",
            "from_date": from_date,
            "to_date": to_date,
            "time_unit": "custom",
            "offset": "0"
        })
        self.g.go('https://www.worksnaps.com/app/detailed_report.cgi?view=dynamic&op_code=new')
        self.g.go(self.g.doc('//*[@id="confirm_download"]/div[2]/a[1]').attr('href'))
        self.g.doc.save(self.__report_file)
        return self.read_report()

    def read_report(self):
        with open(self.__report_file, 'r') as f:
            reader = csv.reader(f)
            report = list(reader)
        return report


        # https://www.worksnaps.com/app/detailed_report.cgi?view=dynamic&op_code=new

