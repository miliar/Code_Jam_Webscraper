__author__ = 'eldos'

testCases = int(input())

for i in range(testCases):
    cfx = input().split()
    c, f, x = [float(val) for val in cfx]
    time = 0.0
    rate = 2.0
    while (x/rate) > (c/rate)+(x/(rate+f)):
        time += c/rate
        rate += f
    else:
        time += x/rate
    print("Case #" + str(i+1) + ": " + str(time))