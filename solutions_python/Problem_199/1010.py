#! coding: utf-8

if __name__ == '__main__':

    #python2:
    T = int(raw_input())
    for i in xrange(T):
        s, K = raw_input().split(" ")
        K = int(K)
        signs = list(s)
        res = 0
        for j in xrange(len(signs) + 1 - K):
            if "+" == signs[j]:
                continue
            else:
                res += 1
                for k in xrange(K):
                    if signs[j + k] == "+":
                        signs[j + k] = "-"
                    else:
                        signs[j + k] = "+"
        if "-" in signs:
            res = "IMPOSSIBLE"
        print("Case #{0}: {1}".format(i + 1, res))



    '''
    #python3:
    T = int(input())
    for i in range(T):
        n, m = [int(s) for s in input().split(" ")]
        res = ""
        print("Case #{0}: {1}".format(i + 1, res))
    '''
