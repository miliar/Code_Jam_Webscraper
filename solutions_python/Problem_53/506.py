from math import pow
data = open('A.txt').readlines()

T = int(data.pop(0))

for i in range(T):
    (N, K) = map(int, data.pop(0).split(' '))
    power = pow(2, N)
    if (K % power) == power - 1:
        print 'Case #%d: %s' % (i+1, 'ON')
    else:
        print 'Case #%d: %s' % (i+1, 'OFF')