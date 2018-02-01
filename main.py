from flask import Flask, render_template, request, redirect
import calendar
from quickstart import push_dinner_to_google, notify_guests

app = Flask(__name__)

@app.route('/')
def pass_through():
    # just redirects to first form so we don't have to type in url path from start
    return redirect('/pick-mon')

@app.route('/pick-mon', methods=['GET', 'POST'])
def month_pick():
    # renders the pick a month form
    return render_template('pick-mon.html')
   
@app.route('/date-meal', methods=['POST'])
def display_month_calendar():
    # writes the html for the calendar of the month user picked for display above the day and meal form
    mon = request.form['month']
    html_cal = calendar.HTMLCalendar()
    cal_x = html_cal.formatmonth(2018, int(mon))
    return render_template('/date-meal.html', cal=cal_x, month=mon)

@app.route('/meal-confirm/<month>', methods=['POST'])
def confirmation(month):
    # displays a confirmation of meal and date 
    meal = request.form['meal']
    date = request.form['date']
    month_by_name = calendar.month_name[int(month)]
    # TODO here is where we would create cal object for google calendar api, more specific dateTime attrib 
    push_dinner_to_google(meal, date)
    return render_template('/meal-confirm.html', m=meal, d=date, month=month_by_name)


if __name__ == "__main__":
    app.run()