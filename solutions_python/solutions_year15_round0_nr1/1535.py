__author__ = 'drex'

T = int(input())

for i in range(T):
    print('Case #{0}: '.format(i+1), end='')
    row1 = input().split()
    row2 = row1[1:]
    s = row2[0]
    count = 0
    pre = 0
    for j in range(len(s)):
        if pre < j:
            count += 1
            pre += 1
        pre += int(s[j])
      
#    print('pre',pre-count)
    print(count)

    

