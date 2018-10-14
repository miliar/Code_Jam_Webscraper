f = open('B-large.in')
w = open('out.txt','w')

T = int(f.readline())
K = T
while T > 0:

    currentline = f.readline().split()
    C = int(currentline[0])#combined
    D = int(currentline[1+C]) #opposed
    N = int(currentline[1+C+1+D])#invoked
    combs = currentline[1:C+1]
    opps = currentline[2+C:1+C+1+D]
    replacements = {}
    #add combs
    for item in combs:
        replacements[item[0]+item[1]] = item[2]
        replacements[item[1]+item[0]] = item[2]
    #perform combos
    invokes = currentline[2+C+1+D:][0].split()
    invokeslist = []
    for letter in invokes[0]:
        invokeslist.append(letter)

    final = []
    for letter in invokeslist:
        if len(final) == 0:
            final.append(letter)
        elif replacements.get(final[len(final)-1] + letter,0) != 0:
            final[len(final)-1] = replacements[final[len(final)-1] + letter]
        else:
            for l in final:
                if l + letter in opps or letter + l in opps:
                    final = []
                    break
            if len(final) != 0:
                final.append(letter)
    #add commas
    i = 1
    while i < len(final):
        final.insert(i,', ')
        i += 2
    final.insert(0,'[')
    final.append(']')
 
    w.write("Case #" + str(K-T+1) + ": " + ''.join(final)+"\n")
    T -= 1

f.close()
w.close()
