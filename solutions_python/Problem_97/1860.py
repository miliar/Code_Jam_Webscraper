'''
Created on Apr 14, 2012

@author: mdoan
'''


with open('input.txt') as f, open('output.txt', 'w') as fout:
    lines = list(f)[1:]
    test = 0
    for line in lines:
        test += 1
        [a, b] = list(map(int, line.split()))
        res = 0
        for m in range(a, b+1):
            for n in range(m+1, b+1):
                s = str(m)
                s1 = str(n) + str(n)
                if s in s1:
                    res += 1
        print('Case #' +str(test) + ': ' + str(res), file = fout)
 