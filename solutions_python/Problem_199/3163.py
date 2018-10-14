def flip(s,k):
    l =list(s)
    i = 0
    while i<k:
        if l[i] == '+':
            l[i] = '-'
        else:
            l[i] = '+'
        i+=1
    return ''.join(l)
def find(s,k,i):
    if '-' not in s:
        return i
    if k > len(s):
        return 'IMPOSSIBLE'
    if s[0] == '-':
        s = flip(s,k)
        i += 1
    return find(s[1:],k,i)
t = int(input())
for a0 in range(t):
    s,k = input().split()
    k = int(k)
    print('Case #'+str(a0+1)+': '+str(find(s,k,0)))
    