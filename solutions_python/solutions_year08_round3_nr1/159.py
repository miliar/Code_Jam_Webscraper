import logging

def outrage(P, L, K, freqs):
    res = 0
    for k in xrange(K):
        for p in xrange(P):
            if k + p*K < L:
                m = int(freqs[k + p*K])*(p+1)
                log.debug('m: ' + str(m))
                res += m
        log.debug('k: ' + str(k) + ' res: ' + str(res))
    return res

def main():
    N = input()
    
    for n in xrange(N):
        data = raw_input().split(' ')
        P = data[0]
        K = data[1]
        L = int(data[2])
        freqs = raw_input().split(' ')
        for i in xrange(L):
            freqs[i] = int(freqs[i])
        freqs.sort(reverse = 1)
        log.debug(freqs)
        print 'Case #' + str(n+1) + ': ' + str(outrage(int(P), int(L), int(K), freqs))
                

if __name__ == '__main__':
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    main()
