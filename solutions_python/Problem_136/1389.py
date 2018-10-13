#r = open('c:\\python27\\codejam\\Inputs.txt')
r = open('c:\\python27\\codejam\\B-large.in')
cases = int(r.readline())

def solve(t,r,c,f,x):
    while x / r > (c / r) + x / (r + f):
        t = t + (c / r)
        r = r + f
    return t + x / r   

with open('c:\\python27\\codejam\\outputs.out', 'w') as w:
    for case in range(1, cases+1):
        nums = r.readline().split()
        c,f,x = float(nums[0]), float(nums[1]), float(nums[2])
        w.write('Case #{0}: {1}\n'.format(str(case), solve(0,2,c,f,x)))
r.close()
