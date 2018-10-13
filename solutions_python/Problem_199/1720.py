def flip(s):
    new = ''
    for ss in s:
        if ss == '+':
            new += '-'
        else:
            new += '+'
    return new
         
t = int(raw_input().strip())

for ti in range(1, t+1):
    s, k = raw_input().strip().split(' ')
    k = int(k)
    count = 0
    
    for i in range(len(s)-k+1):
        if s[i] == '-':
            count += 1
            s = s[:i] + flip(s[i:i+k]) + s[i+k:]
    if '-' not in s:
        answer = str(count)
    else:
        answer = 'IMPOSSIBLE'   
    print 'Case #' + str(ti) + ': ' + answer