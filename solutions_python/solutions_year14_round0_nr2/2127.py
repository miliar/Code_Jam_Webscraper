import sys

filename = sys.argv[1]

def solve(filename):
    fh = open(filename)
    wh = open('B_result_large.txt', 'a')
    times = int(fh.readline().strip())
    case = 1
    while case <= times:
        line = [float(x) for x in fh.readline().strip().split()]
        c = line[0]
        f = line[1]
        x = line[2]
        res = runningTime(c,f,x)
        print("Case #%d: %.7f" % (case, res) , file=wh)
        case += 1
    fh.close()
    wh.close()

def runningTime(c, f, x):
   time = []
   least = x/2
   k = 1
   farmTime = c/(2+(k-1)*f)
   while True:
       t = x/(2 + k*f) + farmTime
       if t < least:
           least = t
           k += 1
           farmTime += c/(2 + (k-1)*f)
       else:
           break
   return least



solve(filename)
