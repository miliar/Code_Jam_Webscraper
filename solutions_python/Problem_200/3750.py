fileName = 'B-large'

def checkTidy(digits):
    isTidy = True
    failIndex = -1
    for i in range(1, len(digits)):
        if digits[i-1] > digits[i]:
            isTidy = False
            failIndex = i-1
            break
    return (isTidy, failIndex)

with open('%s.in' % fileName, 'r') as f, open('%s.out' % fileName, 'w') as g:
    T = int(f.readline())
    for t in range(1, T+1):
        N = int(f.readline().strip())
        lastTidy = N
        if N >= 10:
            digits = [int(d) for d in str(N)]
            numDigits = len(digits)
            isTidy = False
            lastTidy = N
            while not isTidy:
                isTidy, failIndex = checkTidy(digits)
                if isTidy:
                    break
                digits[failIndex] -= 1
                digits[failIndex+1:] = [9 for d in range(1, numDigits - failIndex)]
                lastTidy = int(''.join(map(str, digits)))   
        g.write('Case #%d: %d\n' %(t, lastTidy))
