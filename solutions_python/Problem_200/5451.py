f = open('B-small-attempt0.in')
case = 0

def tidy(num):
    h = num / 100
    t = (num - 100 * h) / 10
    s = num - 100 * h - 10 * t
    if h <= t:
        if t <= s:
            return True
    else:
        return False

for line in f:
    if case == 0:
        case = 1
        continue
    else:
        num = int(line)
        for i in range(num):
            if tidy(num - i):
                print "Case #"+str(case)+':',num - i
                break
    case = case + 1
