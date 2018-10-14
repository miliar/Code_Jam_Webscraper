f=open("C:\Users\Bea\Documents\GCJ\A-small-attempt0.in.txt")
g=open("C:\Users\Bea\Documents\GCJ\A-small-attempt0.out", "w")


c=int(f.readline())

for case in range(c):
    l=f.readline()
    R=""
    for p in l:
        if p=='y': R=R+'a'
        elif p== 'n': R=R+'b'
        elif p== 'f': R=R+'c'
        elif p== 'i': R=R+'d'
        elif p== 'c': R=R+'e'
        elif p== 'w': R=R+'f'
        elif p== 'l': R=R+'g'
        elif p== 'b': R=R+'h'
        elif p== 'k': R=R+'i'
        elif p== 'u': R=R+'j'
        elif p== 'o': R=R+'k'
        elif p== 'm': R=R+'l'
        elif p== 'x': R=R+'m'
        elif p== 's': R=R+'n'
        elif p== 'e': R=R+'o'
        elif p== 'v': R=R+'p'
        elif p== 'z': R=R+'q'
        elif p== 'p': R=R+'r'
        elif p== 'd': R=R+'s'
        elif p== 'r': R=R+'t'
        elif p== 'j': R=R+'u'
        elif p== 'g': R=R+'v'
        elif p== 't': R=R+'w'
        elif p== 'h': R=R+'x'
        elif p== 'a': R=R+'y'
        elif p== 'q': R=R+'z'
        else : R=R+p
        
    g.write("Case #"+str(case+1)+": "+str(R))

f.close()
g.close()
