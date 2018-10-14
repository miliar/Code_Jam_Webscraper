w = "welcome to code jam"
s = raw_input()
cases = int(s)
for case in range(cases):
    s = raw_input()
    cando = [[0] * len(w) for z in range(len(s))]
    for pos in range(len(s)):
        for l in range(len(w)):
            letter = w[l]
            if s[pos] == letter:
                if l == 0:
                    cando[pos][l] += 1
                else:
                    for rpos in range(pos):
                        cando[pos][l] = (cando[pos][l] + cando[rpos][l-1]) % 10000
    c = 0
    for rpos in range(len(s)):
        c = (c + cando[rpos][len(w)-1]) % 10000


    print 'Case #%d: %.4d' % ((case+1), c)

