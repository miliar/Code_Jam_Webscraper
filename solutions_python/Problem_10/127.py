


##################################################################
ifile=file("A-large.in","r")
ofile=file("output.txt","w")

cases=int(ifile.readline())

for case in range(cases):
    print "case: %i/%i" % (case+1, cases)

    lettersKey, keys, alphabet=[int(x) for x in ifile.readline().split()]
    message=[-int(x) for x in ifile.readline().split()]
    message.sort()

    strokes=0
    for position, times in enumerate(message):
        letter=position+1
        keyletter=letter%keys
        if keyletter==0:
            keyletter=keys
        keystrokes=(letter-keyletter)/keys+1
        if keystrokes>lettersKey:
            strokes="IMPOSSIBLE"
            break
        strokes=strokes+(keystrokes*-times)
        #print letter, keys, keyletter, keystrokes

    strokes=str(strokes)
        
    #print strokes

    resultado = "Case #%i: %s" % (case+1, strokes)
    print resultado
    print >> ofile, resultado




ifile.close()
ofile.close()

