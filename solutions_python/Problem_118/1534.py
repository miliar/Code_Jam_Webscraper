# encoding: utf-8

def fair():
#    fnum = []
#    for i in range(10 ** 7):
#        i += 1
#        si = i ** 2
#        if judge(i) and judge(si):
#            fnum.append(si)
    fnum = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004 \
, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, \
404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L,\
1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L,\
1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L,\
1234567654321L, 4000008000004L, 4004009004004L]

    f = open('C-large-1.in')
    ncases = int(f.readline().strip())
    
    for i in range(ncases):
        i += 1
        line = f.readline().split()
        m, n = int(line[0]), int(line[1])
        if m > n:
            m, n = n, m

        cnt = 0
        for num in fnum:
            if m <= num <= n:
                cnt += 1
        print 'Case #%d: %d' % (i, cnt)

        


def judge(num):
    l1 = list(str(num))
    l2 = l1[:]
    l1.reverse()
    return l1 == l2


if __name__ == '__main__':
    import sys
    sys.stdout = open('out.txt', 'w')
    fair()

