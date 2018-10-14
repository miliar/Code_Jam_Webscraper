def buildRemap(s, s1, remap, remapInv):
    for i in range(0, len(s)):
        c = s[i]
        c1 = s1[i]
        if c != ' ' and c1 != ' ':
            remap[ord(c) - ord('a')] = c1
            remapInv[ord(c1) - ord('a')] = c

def __main__():
    remap = [-1 for _ in range(ord('a'), ord('z') + 1)]
    remapInv = [-1 for _ in range(ord('a'), ord('z') + 1)]
    s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    s11 = "our language is impossible to understand"
    buildRemap(s1, s11, remap, remapInv)
    s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    s21 = "there are twenty six factorial possibilities"
    buildRemap(s2, s21, remap, remapInv)
    s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    s31 = "so it is okay if you want to just give up"
    buildRemap(s3, s31, remap, remapInv)
    
    remap[ord('z') - ord('a')] = 'q'
    remap[ord('q') - ord('a')] = 'z'
    
    f = open("A-small-attempt0.in", "rt")
    N = int(f.readline())
    
    fout = open("A.out", "wt+")
    
    for t in range(0, N):
        s = f.readline().strip('\n')
        s1 = ""
        for i in range(0, len(s)):
            c = s[i]
            if c != ' ':
                s1 += remap[ord(c) - ord('a')]
            else:
                s1 += ' '
        fout.write("Case #%(case)s: %(result)s\n" % {"case": t + 1, "result": s1})

if __name__ == "__main__":
    __main__()