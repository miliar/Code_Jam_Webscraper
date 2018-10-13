import sys
N = int(sys.stdin.readline())

for caseNumber in range(1,N+1):
    line = sys.stdin.readline().rstrip('\n').split(' ')
    P = int(line[0])
    K = int(line[1])
    L = int(line[2])
    line = sys.stdin.readline().rstrip('\n').split(' ')
    freq = []
    for i in line:
        freq.append(int(i))
    freq.sort()
    freq.reverse()
    
    if len(freq) > P*K:
        print 'Case #%s: %s' % (caseNumber, "impossible")
        continue
    
    totalKeyPresses = 0
    k = 1
    p = 1
    for i in freq:
        totalKeyPresses += p*i
        k += 1
        if k > K:
            p+=1
            k=1
    
    print 'Case #%s: %s' % (caseNumber, totalKeyPresses)
