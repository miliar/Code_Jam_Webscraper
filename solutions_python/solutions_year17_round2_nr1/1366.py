#!/usr/bin/python3

def timeToDest(dest, current, speed):
    return (dest - current) / speed

def velocity(distance, time):
    return distance / time

times = []

t = int(input())
for i in range(1, t + 1):
    dest, horseCount = [int(s) for s in input().split(" ")]
    for j in range(0, horseCount):
        location, speed = [int(s) for s in input().split(" ")]
        times.append(timeToDest(dest, location, speed))
    anniesSpeed = velocity(dest, max(times))
    print("Case #{}: {}".format(i, anniesSpeed))
    times = []
