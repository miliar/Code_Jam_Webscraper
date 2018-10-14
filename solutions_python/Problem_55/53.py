import sys
import math

def solve(R, k, gi):
    N = len(gi)
    next = [-1] * N
    income = [-1] * N
    last_count = [-1] * N
    last_money = [-1] * N
    count = 0
    pos = 0
    period = -1
    money = 0
    while count<R:
        if period<0 and next[pos]>=0:
            period = count - last_count[pos]
            delta = money - last_money[pos]
            m = (R - count) // period
            count += m*period
            money += m*delta
        else:
            if next[pos]>=0:
                count += 1
                money += income[pos]
                pos = next[pos]
            else:
                last_count[pos] = count
                last_money[pos] = money
                count += 1
                newpos = (pos + 1) % N
                people = gi[pos]
                while newpos!=pos:
                    people += gi[newpos]
                    if people > k:
                        people -= gi[newpos]
                        break
                    newpos = (newpos + 1) % N
                income[pos] = people
                next[pos] = newpos
                money += people
                pos = newpos
    return money

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    R = int(line[0])
    k = int(line[1])
    N = int(line[2])
    line = input.readline().strip(' \r\n\t').split()
    gi = [int(line[i]) for i in range(N)]
    res = solve(R, k, gi)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
    
