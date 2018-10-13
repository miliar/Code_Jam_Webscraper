f = open('D-large.in', 'r')
outf = open('output4large.txt', 'w')

T = int(f.readline())

def deceitful(together):
    n = len(together)

    ind_head = 0
    ind_tail = n - 1
    head_sum = 0
    while ind_head <= ind_tail:
        if head_sum <= 0:
            head_sum += together[ind_head][1]
            ind_head += 1
        else:
            if together[ind_tail][1] == -1:
                head_sum -= 1
                n -= 2
            ind_tail -= 1
    return n / 2

def war(together):
    n = 0

    ind_head = 0
    ind_tail = len(together) - 1
    tail_sum = 0
    while ind_head <= ind_tail:
        if tail_sum <= 0:
            tail_sum += together[ind_tail][1]
            ind_tail -= 1
        else:
            if together[ind_head][1] == -1:
                tail_sum -= 1
                n += 1
            ind_head += 1
    return n                

for test_ind in range(T):
    N = int(f.readline())
    naomi = map(float, f.readline().split())
    ken = map(float, f.readline().split())
    together = zip(naomi, [1] * N) + zip(ken, [-1] * N)
    together.sort()

    out_str = ('Case #' + str(test_ind + 1) + ': ' + str(deceitful(together)) + ' ' +
               str(war(together))+ '\n')
    outf.write(out_str)

f.close()
outf.close()
