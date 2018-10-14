def flip(S, i, K):
    for j in xrange(K):
        S[i+j] = '-' if S[i+j] is '+' else '+'

def main(index):
    print 'Case #%d:' % index,
    S, K = raw_input().split(' ')
    K = int(K)
    S = list(S)

    counter = 0
    for i in xrange(len(S)-K+1):
        if S[i] is '-':
            counter += 1
            flip(S, i, K)



    if '-' in S:
        print 'IMPOSSIBLE'
    else:
        print counter

T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
