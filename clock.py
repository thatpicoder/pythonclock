import time

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if time.daylight:
        tz = time.tzname[1]
    else:
        tz = time.tzname[0]
    full_time = current_time + " " + tz
    print("python clock, made by bitetheapple")
    print('\rCurrent Time: ' + full_time, end='', flush=True)
    time.sleep(1)
