# f = open('B-large.in')
# it = iter(f)
# def read():
#     return next(it)
# of = open('q2-large.out', 'w')
#  
# def write(s):
#     print(s, file=of)

def write(s):
    print(s)
def read():
    return input()


def solve(c, f, x):
    r = 2
    time = 0
    while True:
        thistime = x/r
        nextime = c/r + x/(r+f)
        
        if thistime <= nextime:
            return time + thistime
        time += c/r
        r += f
        

ntests = int(read())
for i in range(ntests):
    res = solve(*(float(i) for i in read().split()))
    write('Case #{}: {}'.format(i+1, res))
