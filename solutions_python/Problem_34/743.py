L, D, N = map(int,raw_input().split(" "))
fout = file("alien.out","w")
words = []

for i in xrange(D):
    word = raw_input()
    words.append(word)

for k in xrange(N):

    Str = raw_input()
    newStr = []
    tmp = ''
    leng = len(Str)
    group = False

    for i in xrange(leng):
        if Str[i] == "(":
            group = True
            tmp = ''
        elif Str[i] == ")":
            newStr.append(tmp)
            group = False
        else:
            if group == True:
                tmp += Str[i]
            else:
                newStr.append(Str[i])
                

    #print newStr
    count = 0
    for i in xrange(D):
        #print "i = ", i
        cond = True
        for j in xrange(L):
            #print "j =", j
            if words[i][j] not in newStr[j]:
                cond = False
                break
        if cond == True:
            count += 1

    fout.write("Case #" + str(k+1) + ": " + str(count)+"\n")

fout.close()


    
