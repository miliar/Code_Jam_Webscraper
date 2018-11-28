# Input should be placed in file B.txt

def pos(hour, minut):
    return hour * 60 + minut

endOfTheDay = 24 * 60

f = open('B.txt')
N = int(f.readline())
for case in range(N):
    print "Case #%d:" % (case+1,),
    T = int(f.readline())
    NA, NB = map(int, f.readline().split())
    a = [0] * endOfTheDay
    b = [0] * endOfTheDay
    for t in range(NA):
        depart, arrive  = f.readline().split()
        hd, md = map(int, depart.split(':'))
        ha, ma = map(int, arrive.split(':'))
        for i in range(pos(hd, md), endOfTheDay):
            a[i] += 1
        ready = pos(ha, ma)+T
        if ready < endOfTheDay:
            for i in range(ready, endOfTheDay):
                b[i] -= 1
    for t in range(NB):
        depart, arrive  = f.readline().split()
        hd, md = map(int, depart.split(':'))
        ha, ma = map(int, arrive.split(':'))
        for i in range(pos(hd, md), endOfTheDay):
            b[i] += 1
        ready = pos(ha, ma)+T
        if ready < endOfTheDay:
            for i in range(ready, endOfTheDay):
                a[i] -= 1
    print max(a), max(b)

