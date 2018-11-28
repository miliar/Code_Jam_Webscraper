#! coding: utf-8

def digits(i_n, io_digs):
    while i_n > 0:
        io_digs.append(i_n % 10)
        i_n = int(i_n / 10)

if __name__ == '__main__':

    #python2:
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())

        digs = []
        digits(N, digs)

        j = 1
        while j < len(digs):
            if digs[j - 1] < digs[j]:
                digs[j] -= 1
                digs[:j] = [9] * j
            j += 1

        res = 0
        k = 1
        for j in digs:
            res += j * k
            k *= 10
        
        print("Case #{0}: {1}".format(i + 1, res))

    '''
    #python3:
    T = int(input())
    for i in range(T):
        n, m = [int(s) for s in input().split(" ")]
        res = ""
        print("Case #{0}: {1}".format(i + 1, res))
    '''
