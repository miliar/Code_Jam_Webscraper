import sys

def pancake(input_s, input_k):
    k = int(input_k)
    s = [0] * (len(input_s))
    for i in range(len(input_s)):
        if input_s[i] == '+':
            s[i] = 1
        else:
            s[i] = 0
    
    count = 0
    for i in range(len(s) - k + 1):
        if s[i] == 0:
            count += 1
            for j in range(k):
                s[i + j] = 1 - s[i + j]
                
    for i in range(len(s) - k + 1, len(s)):
        if s[i] == 0:
            return -1
    return count    
    
    
cin = open('A-small-attempt0.in', 'r')
cout = open('A-small-attempt0.out', 'w')
n = int(cin.readline())
for i in range(n):
    input_s, input_k = cin.readline().split()
    ans = pancake(input_s, input_k)
    if ans == -1:
        cout.write('Case #' + str(i) + ': IMPOSSIBLE \n')
    else:
        cout.write('Case #' + str(i) + ': ' + str(ans) + '\n')
cin.close()
cout.close()
