import sys
import math

N = 0
L = ""
T = 1
A = 0
B = 0
def getCaseData(fp):
    global L, A, B
    L = fp.readline()
    L = L.replace("\n", "")
    L = L.split(" ")
    A = int(L[0])
    B = int(L[1])

def getItems():
    global N, L, T, A, B
    #print A, B
    fas = 0
    for i in range(A,B+1):
        p = math.sqrt(i)
        stri = str(i)
        if p % 1 == 0:
            strp = str(int(p))
            if isPalindrome(stri,0,len(stri)-1):
                if isPalindrome(strp,0, len(strp)-1):
                    fas += 1
                    #print "*** FAS: {0} ***\n".format(fas)


    print "Case #{0}: {1}".format(int(T), fas)

def isPalindrome(string,a,z):
    #Debug
    #print "String: {0}\na: {1}\nb: {2}\nlength: {3}\n".format(string,a,z,len(string))
    if string[a] == string[z]:
        if (a - z) > 1:
            return isPalindrome(string,a+1, z-1)
        else:
            return True
    return False

def main(argv):
    global N, L,T
    infile = argv[0]
    #open file
    fp = open(infile)

    N = fp.readline()
    for i in range(0, int(N)):
        getCaseData(fp)
        getItems()
        T += 1

if __name__ == "__main__":
    main(sys.argv[1:])
