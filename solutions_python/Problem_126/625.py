def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result *= (n+1) / i -1
    return int(result)

def part(word, n):
    i=0
    for x in word:
        if x:
            i+=1
            if i>=n:
                return 1
        else:
            i=0
    return 1 if i>=n else 0

def func(word, n):
    c=0
    word=tuple(0 if x in "aeiou" else 1 for x in word)
    
    for i in range(len(word)+2-n):
        for j in range(i+n, len(word)+1):
            c+=part(word[i:j], n)
    return c

file=open(r"C:\Users\user\Downloads\A-small-attempt0 (2).in").read().splitlines()[1:]
i=1
for line in file:
    line=line.split(' ')
    print("Case #"+str(i)+":", func(line[0], int(line[1])))
    i+=1
