def add_time(start, duration, day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

    time_part, period = start.split()
    start_hour, start_min = map(int, time_part.split(':'))
    dur_hour, dur_min = map(int, duration.split(':'))

    if period == 'PM' and start_hour != 12:
        start_hour += 12
    if period == 'AM' and start_hour == 12:
        start_hour = 0

    total_minutes = start_min + dur_min
    extra_hours = total_minutes // 60
    final_min = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hours
    days_passed = total_hours // 24
    final_hour = total_hours % 24

    if final_hour == 0:
        display_hour = 12
        new_period = 'AM'
    elif final_hour < 12:
        display_hour = final_hour
        new_period = 'AM'
    elif final_hour == 12:
        display_hour = 12
        new_period = 'PM'
    else:
        display_hour = final_hour - 12
        new_period = 'PM'

    result = f'{display_hour}:{final_min:02d} {new_period}'

    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        result += f', {days_of_week[new_day_index]}'

    if days_passed == 1:
        result += ' (next day)'
    elif days_passed > 1:
        result += f' ({days_passed} days later)'

    return result
