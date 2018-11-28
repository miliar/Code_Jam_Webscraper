f = open('/Users/simple/Desktop/A-large.in')
L, D, N = map(int, f.readline().split())
dics = [ f.readline().strip() for i in range(D)]
for i in range(N):
    line = f.readline().strip()
    words = []
    word = []
    is_paran = False
    for c in line:
        if c == '(':
            is_paran = True
            continue
        if c == ')':
            is_paran = False
            words.append(word)
            word=[]
            continue
        if (is_paran) :
            word.append(c)
        else:
            words.append(c)
    #print(words)
    result = 0
    for w in dics:
        match_all = True
        for j, c in enumerate(w):
            if c not in words[j]:
                match_all = False
        if match_all:
            result += 1

    print('Case #{}: {}'.format(i+1, result))
