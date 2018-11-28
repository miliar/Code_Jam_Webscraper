import sys

filename = sys.argv[1]

def solve(filename):
    fh = open(filename)
    wh = open('B_result.txt', 'a')
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
   time.append(x/2)
   k = 1
   while True:
       t = x/(2 + k*f) + sum(c/(2+(i-1)*f) for i in range(1, k+1))
       if t < time[k-1]:
           time.append(t)
           k += 1
       else:
           break
   return time[k-1]



solve(filename)
