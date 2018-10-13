__author__ = 'Narrenschyff'
f = open("B-large.in", "r")
o = open("outputA","w")
N = int(f.readline())
for i in range(1,N+1):
    nums = f.readline().split()
    C = float(nums[0])

    F = float(nums[1])
    X = float(nums[2])
    total = 0.0
    cookiesPerS = 2.0

    time = 0
    while(total < X):


        if((C/cookiesPerS +(X)/(cookiesPerS+F)) >=(X/cookiesPerS)):

            total = ((X)/(cookiesPerS)) * cookiesPerS
            time = time + (X)/cookiesPerS

            o.write("Case #"+str(i)+": "+str(round(time, 7))+"\n")
            break
        else:
            total = 0

            time = time + C/cookiesPerS
            cookiesPerS = cookiesPerS + F

