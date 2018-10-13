__author__ = 'Raullen'

f = open('C-small-practice.in','r')
T = int(f.readline())
g = open('res.out','w')
res = list()

for case in range(T):
    tmp = f.readline().strip('\n').split(' ')
    N = int(tmp[0])
    S = int(tmp[1])
    p = int(tmp[2])
    arr = [int(x) for x in tmp[3:]]
    arr.sort()
    arr.reverse()

    cnt = 0
    for x in arr:
        x = x
        if x >= 3*p or x == 3*p-1 or  x == 3*p-2:
            cnt += 1

        if x == 3*p-3 or x == 3*p-4:
            if S > 0 and x>2:
                S -= 1
                cnt += 1
            else:
                break

        if x<=3*p-5:
            break

    print 'Case #'+ str(case+1)+': '+ str(cnt)

g.writelines(res)
g.close()
f.close()