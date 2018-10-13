import sys

number = sys.stdin.readline()
test_cases = int(number)

def area(r):
    return r**2 - (r-1)**2

for test_no in range(1, test_cases + 1):
    line = sys.stdin.readline().split(" ")
    r = int(line[0])
    t = int(line[1])

    n = 1
    r += 1
    sum = area(r)
    while sum <= t:
        r+=2
        n+=1
        sum += area(r)

    print "Case #"+ str(test_no) + ": " + str(int(n-1))