def flip(c):
    if c == '+':
        return '-'
    else:
        return '+'

def flip_sub(s,i,j):
    s = [char for char in s]
    for i in range(i,j+1):
        s[i] = flip(s[i])
    return ''.join(s)

def flip_to_happy(s,k):
    s = [x for x in s]
    flips = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            flips += 1
            s = flip_sub(s,i,i+k-1)
    if len(set(s)) == 1:
        return flips
    else:
        return 'IMPOSSIBLE'

t = int(input())
for i in range(t):
    s,k  = input().split(' ')
    k = int(k)
    print("Case #"+str(i+1)+": "+str(flip_to_happy(s,k)))
