def rotate(num, shift):
    num = str(num)
    return int(num[len(num)-shift:] + num[:len(num)-shift])

#uniq_mn = []

T = int(raw_input())
#T = 1

for tc in range(T):
    uniq_mn = []
    A, B = map(int, raw_input().split())
    #A, B = 1111, 2222
    len_num = len(str(A))
    for n in range(A, B+1):
        for i in range(len(str(n))-1, 0, -1):
            m = rotate(n, i)
            if (A <= n < m <= B):
                if (n, m) not in uniq_mn and (len(str(n)) == len(str(m)) == len_num):
                    uniq_mn.append((n, m))
    print 'Case #%d: %s' % (tc+1, len(set(uniq_mn)))
