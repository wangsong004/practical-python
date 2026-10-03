# bounce.py
#
# Exercise 1.5

time=0
total_time=10
height=100.0
ratio=0.6
while time<total_time:
    height=height*ratio
    time+=1
    print(time,round(height,4))