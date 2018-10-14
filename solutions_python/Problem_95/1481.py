import sys


def main ():
    noCases = int(sys.stdin.readline())
    ex = [["ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"],["rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"],["de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"]]
    for i in xrange(1,noCases+2):
        case = sys.stdin.readline()
        result = ""
        for j in xrange(0,len(case)):
            cchar = case[j]
            if cchar == "\n":
                break
            if cchar == " ":
                result += " "
                continue
            if cchar == "q":
                result += "z"
                continue
            if cchar == "z":
                result += "q"
                continue
            found = False;
            for k in xrange(0,len(ex)):
                for l in xrange(0,len(ex[k][0])):
                    if(ex[k][0][l] == case[j] and not found):
                        found = True
                        result += ex[k][1][l]
                        break
            if not found:
                result  += "?"
                
        print "Case #" + str(i) + ": " + result
        
    exit()

if __name__ == "__main__":
    main()