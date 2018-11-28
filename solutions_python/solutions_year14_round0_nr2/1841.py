__author__ = 'nguyensontung1404'

def decideBuy(rate, c, f, x):
    if x / rate < x / (rate+f) + c/rate:
        return False
    else:
        return True

def find_time(c, f, x):
    rate = 2.0
    time = 0
    if x <= c:
        return x / rate
    else:
        while decideBuy(rate, c, f, x):
           time += c / rate
           rate += f
        return time + x / rate

if __name__ == "__main__":
    import sys
    sys.stdin = open("B-large.in")
    sys.stdout = open("outputlarge.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        _str = sys.stdin.readline()
        c, f, x = map(float, _str.split(" "))
        print "Case #%d:" % (case), find_time(c, f, x)
