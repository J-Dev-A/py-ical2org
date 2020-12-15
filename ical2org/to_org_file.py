import datetime
import calendar
import os

ORG_PATH = '/Users/jd/org/work'


def write_as_org(org_dict):
    today = datetime.date.today()
    month = calendar.month_name[today.month]

    _today_month = str(today.month)
    if len(_today_month) < 2:
        _today_month = f'0{_today_month}'

    _today_day = str(today.day)
    if len(_today_day) < 2:
        _today_day = f'0{_today_day}'

    _today = f'{str(today.year)}{_today_month}{_today_day}'

    year_folder_name = str(today.year)
    year_folder_path = f'{ORG_PATH}/{year_folder_name}'

    month_folder_name = f'{today.month} {month}-{today.year}'
    month_folder_path = f'{year_folder_path}/{month_folder_name}'
    file_path = f'{month_folder_path}/{_today}.org'

    # check folder presence
    year_folder_exists = os.path.isdir(year_folder_path)
    month_folder_exists = os.path.isdir(month_folder_path)
    file_exists = os.path.isfile(file_path)

    # if folder is not present, create one
    if not year_folder_exists:
        os.mkdir(year_folder_path)
        year_folder_exists = True

    if not month_folder_exists:
        os.mkdir(month_folder_path)
        month_folder_exists = True

    if year_folder_exists and month_folder_exists and not file_exists:
        with open(file_path, 'a') as today_file:
            file_defaults = f'#+TITLE: {_today}\n'
            timestamp_str = f'{today.strftime("%Y-%m-%d")} {calendar.day_abbr[today.weekday()]} {datetime.datetime.now().strftime("%H:%M")}'
            file_defaults += f'#+CREATED: [{timestamp_str}]\n'
            file_defaults += f'#+LAST_MODIFIED: [{timestamp_str}]\n'
            file_defaults += f'#+FILETAGS: :work:\n\n'
            file_defaults += f'* {calendar.day_name[today.weekday()]}, {month} {today.day} {today.year}\n\n'
            file_defaults += f'** Meetings\n\n'
            for each in org_dict:
                file_defaults += f'*** {org_dict[each]}\n'
                file_defaults += f'SCHEDULED: {each.rstrip("_")}\n'
            today_file.write(file_defaults)
            print(f'Org file can be accessed at {file_path}')

    if file_exists:
        print('File already created for the day, check the Foam workspace')
