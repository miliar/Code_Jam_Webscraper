def solve(s, p, totals):

    l1 = max(0, p * 3 - 2) # any total above this number can be (p-1, p-1, p) with no surprise 
    l2 = max(0, p * 3 - 4) # otherwise, it can be (p-2, p-2, p) for a win with a surprise

    i = 0
    
    for t in totals:
        if p > 0 and t == 0:
            continue
        if t >= l1:
            i += 1
        elif t >= l2 and s > 0:
            i += 1
            s -= 1

    return i

def parse(s):
    l = map(int, s.split(" "))
    return l[1], l[2], l[3:]

if __name__ == "__main__":

    count = int(raw_input())
    for i in range(count):
        s = raw_input()

        print 'Case #%d: %s' % ((i+1), solve(*parse(s)))


