readfromline = lambda func : [func(input) for input in str(raw_input()).split()]

if __name__ == '__main__':
    N=int(raw_input())
    for case in range(N):
        P, K, L = readfromline(int)
        freqs=[int(freq) for freq in str(raw_input()).split()]
        freqs.sort()
        freqs.reverse()
        tot=0
        for i in range(len(freqs)):
            tot+=freqs[i]*(i/K+1)
        print 'Case #'+str(case+1)+': '+str(tot)
