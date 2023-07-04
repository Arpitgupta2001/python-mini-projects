import time
timestamp = int(time.strftime('%H'))
print(timestamp)
if( timestamp >= 12 ):
    if(timestamp < 18):
        print("Good AfterNoon")
    else:
        print("Good Evening")
else:
    print("Good Morning")
