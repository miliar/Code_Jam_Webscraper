# L=length, D=lines, N = test cases
f = file('sample.in','r')
(L,D,N) = map(int,f.readline().split(' '))

words = {}
for x in xrange(D):
    word = f.readline().strip()
    v = words
    k = 0
    for y in word:
        k = k + 1
        if not y in v: v[y] = {}
        v = v[y]

def solve(letters,base,level):
    if level == 0: return 1
    success = 0
    for l in letters[0]:
        if l in base:
            success += solve(letters[1:],base[l],level-1)
    return success
        

    
for x in xrange(N):
    word = f.readline().strip()
    l = 0
    letters = []
    for w in range(L):
        if word[l] == '(':
            r = word.index(')',l)
            letters.append(word[l+1:r])
            l = r+1
        else:
            letters.append(word[l])
            l = l +1
    print 'Case #'+str(x+1)+':',solve(letters,words,L)

