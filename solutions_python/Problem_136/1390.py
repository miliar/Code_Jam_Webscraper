import os, math

def getTime(C, F, X):
    
    speed = 2.0
    if C >= X:
        return X / speed
    
    k = int(math.ceil((X * F - 2 * C) / (C * F)))
    time_elapsed = .0
    for i in xrange(0, k - 1):
        time_elapsed += (C / speed)
        speed += F
    time_elapsed += (X / speed)
    """
    time_to_upgrade = C / speed
    time_left = X / speed
    time_elapsed = .0
    
    while True:
        #each time decide wether to buy a new farm
        time_elapsed += time_to_upgrade
        time_left -= time_to_upgrade
        speed += F
        time_left_new = X / speed
        if time_left_new >= time_left:
            break;
        time_to_upgrade = C / speed
        time_left = time_left_new
    
    time_elapsed += time_left
    """
    return time_elapsed

f = open("B-large.in", 'r')
n_cases = int(f.readline().strip())

for i, line in enumerate(f):
    arr = line.strip().split()
    print "Case #{0}: {1:.7f}".format(i+1, getTime(float(arr[0]), float(arr[1]), float(arr[2])))


