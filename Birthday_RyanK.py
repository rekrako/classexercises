import datetime as dt
dayBorn=int(input('what day of the months were you born in: '))
monthBorn=int(input('what month were you born in: '))
yearBorn=int(input('what year were you born in: '))
db=dt.date(yearBorn,monthBorn,dayBorn)

if __name__ != '__main__':
    dbFormatted=db.strftime("%d of %B, on a %A, in %Y")
    print('\nYou were born on the ', dbFormatted)