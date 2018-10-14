
__author__ = 'koko'



import fileinput


def filltab(intab, start):
    i = start
    ilen = len(intab)
    while i<ilen:
        intab[i]=9
        i+=1


def tidyup(inp):
    intab = str(inp)
    outtab = [int(el) for el in intab]
    i=0
    ilen = len(intab)-1
    result = inp
    while i<ilen:
        if outtab[i]>outtab[i+1]:
            filltab(outtab,i+1)
            outtab[i] -=1
            badtab = [str(el) for el in outtab]
            result = tidyup(''.join(badtab)) ## this is veryveryvery bad
            break
        i+=1
    return result

if __name__ == "__main__":
    cases = int(input())
    for t in range(1, cases + 1):
        kok = raw_input()
        #print(kok)
        result = tidyup(kok)
        print("Case #"+ str(t) + ": " + str(int(result)))
