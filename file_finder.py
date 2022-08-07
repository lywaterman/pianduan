import os
import datetime


def get_date_by_precision(date, precision):
    year = date.year
    month = date.month
    day = date.day
    if precision == "year":
        month = 1
        day = 1
    elif precision == "month":
        day = 1

    return date.replace(minute=0, hour=0, second=0, year=year, month=month, day=day)


def compare_date(start_date, year, month=1, day=1):
    date = "{0}/{1}/{2}".format(year, month, day)
    date_time_obj = datetime.datetime.strptime(date, '%Y/%m/%d')
    return date_time_obj >= start_date


def find_date_dir(res_list, basedir, year, date, precision):
    start_date = get_date_by_precision(date, precision)

    yeardir = os.path.join(basedir, year)
    if precision == "year":
        if compare_date(start_date, year):
            res_list.append(yeardir)
            return

    for month in os.listdir(yeardir):
        mouthdir = os.path.join(yeardir, month)
        if precision == "month":
            if compare_date(start_date, year, month):
                res_list.append(mouthdir)
        elif precision == "day":
            for day in os.listdir(mouthdir):
                daydir = os.path.join(mouthdir, day)
                if compare_date(start_date, year, month, day):
                    res_list.append(daydir)


if __name__ == "__main__":
    date_time_obj = datetime.datetime.strptime("2022", '%Y')
    res = []
    find_date_dir(res, "/Users/ly/test", "2022", datetime.datetime.now(), "day")
    print(res)
