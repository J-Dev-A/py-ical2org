import os
import datetime
import calendar
from .to_org_file import write_as_org


def main():
    stream = os.popen(
        'icalBuddy -b "*" -npn -iep "title,datetime" -ps "| : |" -po "datetime,title"  -ic "Calendar" -nc eventsToday')
    output = stream.read()
    lines = output.split('\n')
    line_array = [line[1:] for line in lines if line[1:2].isdigit()]

    today = datetime.date.today()
    to_file_arr = [
        f'<{datetime.datetime.today().strftime("%Y-%m-%d")} {calendar.day_abbr[today.weekday()]} {line[:line.find(" ")]}> {line[line.rfind(" :"):]}'
        for line in line_array
    ]

    org_dict = {}
    for entry in to_file_arr:
        entry = entry.split(' : ')
        if org_dict.get(entry[0]):
            org_dict[f'{entry[0]}_'] = entry[1]
        else:
            org_dict[entry[0]] = entry[1]
    print(org_dict)
    write_as_org(org_dict)
