import sys, re

def solve(c, f, x):
    if c >= x:
        return x / 2
    k = 0
    t = 0.0
    while True:
        t += c / (2 + k * f)
        if x >= (x-c)*(2+(k+1)*f)/(2+k*f):
            return t + (x-c)/(2+k*f)
        else:
            k += 1


def main(filename):
    with open(filename) as f_in:
        total = int(f_in.readline())
        for i in range(1, total+1):
            c, f, x = map(float, f_in.readline().strip().split(' '))
            print 'Case #{0}: {1:.7f}'.format(i, solve(c, f, x))
            

if __name__ == "__main__":
    main(sys.argv[1])
