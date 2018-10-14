#!/usr/bin/python
def possibilities(mark, p):
    if p == 0:
        return (1,0)
    elif p == 1:
        if mark>0:
            return (1,0)
        else:
            return (0,0)
    else:
        minrequired = p + (p - 1) + (p - 1)
        if mark >= minrequired:
            return (1,0)
        minrequired = p + (p - 2) + (p - 2)
        if mark >= minrequired:
            return (1,1)
        return (0,0)
if __name__ == "__main__":
    f = open('B-large.in', 'r')
    t = int(f.readline())
    i = 1
    for line in f:
        x = [int(s) for s in line.split()]
        n = x[0]
        s = x[1]    
        p = x[2]
        marks = x[3:]
        nums = 0
        for m in marks:
            a = possibilities(m, p)
            if a[0] == 1:
                if a[1] == 1:
                    if s > 0:
                        s -= 1
                        nums += 1
                    else:
                        pass
                else:
                    nums += 1
        print "Case #"+str(i)+": "+str(nums)
        i += 1
    f.close()