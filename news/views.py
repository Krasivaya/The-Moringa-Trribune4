from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt

# News View
def welcome(request):
    return render(request, 'welcome.html')

#News view for particular day
def news_of_day(request):
    date = dt.date.today()

    #Function to convert date number to exact day name
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

#Getting Date of a week
def convert_dates(dates):
    #function to get weekdays for date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Return days
    day = days[day_number]
    return day

#Passt days News View
def past_days_news(request, past_date):
    try:
        #convert data from url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #raise 404 error when valueError is thrown
        raise Http404()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)