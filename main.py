import time
def Countdown(t):
  while t>0:
    print(t)
    t = t - 1
    time.sleep(1)
  print ("Time's Up")

print ("Enter a time to start with")
Seconds = input()
while not Seconds.isdigit():
    print ("Error! Please enter a digit")
    Seconds = input()
Seconds = int(Seconds)
Countdown(Seconds)