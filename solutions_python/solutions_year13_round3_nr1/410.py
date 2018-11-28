
def substr(s):
    j = 1
    a = list()
    while True:
        for i in range(len(s)-j+1):
            a.append(s[i:i+j])
        if j == len(s):
            break
        j+=1
    return a

T = int(raw_input())
vowels = "aeiou"
for i in range(T):

    line = raw_input().split()
    s = line[0]
    n = int(line[1])

    result = 0
    for ss in substr(s):
        conseq = 0
        maxconseq = 0
        for sss in ss:
            if sss not in vowels:
                conseq+=1
            else:
                conseq = 0
            if conseq > maxconseq:
                maxconseq = conseq
        if maxconseq >= n:
            result += 1

    print "Case #%d: %d" % (i+1, result)

