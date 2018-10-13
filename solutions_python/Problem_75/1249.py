T=input()
for j in range(1,T+1):
    combos={}
    pairs={}
    strings=raw_input().split()
    C=int(strings[0])
    D=int(strings[C+1])
    for e in strings[1:C+1]:
        combos[e[:-1]]=e[-1]
        combos[e[::-1][1:]]=e[-1]
    for e in strings[C+2:C+D+2]:
        pairs[e[0]]=e[1]
        pairs[e[1]]=e[0]
    final=[]
    for i in strings[-1]:
#        print final,i
        if len(final) is not 0 and (final[-1]+i) in combos:
            final[-1]=combos[final[-1]+i]
            continue
        if i in pairs and pairs[i] in final:
            final=[]
            continue
        final+=[i]
    print ("Case #%d:"%j),''.join(c for c in str(final) if c is not "'")

