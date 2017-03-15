import sys
import os
import csv
from models import Bills

csv_path = '/User/Friese/CODE/tiy/week_4/first-django-app/mysite/bills/bills.csv'
project_home = '/Users/Friese/CODE/tiy/week_4/first-django-app/mysite'


sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

dataReader = csv.reader(open(csv_path), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'BILL':
        bill = Bills()
        bill.bill = row[0]
        bill.bill = row[1]
        bill.bill = row[2]
        bill.save()
