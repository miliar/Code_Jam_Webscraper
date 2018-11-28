import math

def main():
    print("hi")
    
    f = open('C-small-attempt1.in', 'r')
    numberOfProblems = int(f.readline())
    out = open('C-small-attempt1.out','w')
    for x in range(0,numberOfProblems):
        T,L = f.readline().split(" ")
        T = int(T)
        L = int(L)

        X = f.readline().replace("\n","")
        X = X * L

        count = 0
        found = False
        lasti = -1
        lastj = 1
        answer = ""
        jkStr = ""
        kStr = ""
        fin = ""
        while not found:
            
            jkStr,lasti = searchFrontFor(X,'i',lasti)
            if jkStr != "FAIL":
                kStr,lastj = searchFrontFor(jkStr,'j',0)
            else:
                answer = "NO"
                break
            if kStr != "FAIL":
                fin,last = stringEquiv(kStr,'k')
            else:
                answer = "NO"
                break

            if fin != "FAIL":
                answer = "YES"
                break
            else:
                answer = "NO"
                break

            
            
        
        

        
        #write answer to out
        out.write("Case #" + str(x+1) + ": " + str(answer) + "\n")



    f.close()
    out.close()

def stringEquiv(strIn,val):
    curVal = strIn[0]
    for x in range(1, len(strIn)):
        curVal = mult(curVal,strIn[x])
    if curVal == val:
            return "",len(strIn)
    return "FAIL",0

def searchFrontFor(strIn, val, minLength):
    curVal = strIn[0]
    for x in range(1, len(strIn)):
        if curVal == val and x > minLength:
            return strIn[x:],x
        curVal = mult(curVal,strIn[x])
    if curVal == val and len(strIn) > minLength:
            return "",len(strIn)
    return "FAIL",0


def mult(val1,val2):
    if val1 == '1':
        if val2 == '1':
            return '1'
        elif val2 == 'i':
            return 'i'
        elif val2 == 'j':
            return 'j'
        elif val2 == 'k':
            return 'k'

    elif val1 == 'i':
        if val2 == '1':
            return 'i'
        elif val2 == 'i':
            return '-1'
        elif val2 == 'j':
            return 'k'
        elif val2 == 'k':
            return '-j'
        
    elif val1 == 'j':
        if val2 == '1':
            return 'j'
        elif val2 == 'i':
            return '-k'
        elif val2 == 'j':
            return '-1'
        elif val2 == 'k':
            return 'i'

    elif val1 == 'k':
        if val2 == '1':
            return 'k'
        elif val2 == 'i':
            return 'j'
        elif val2 == 'j':
            return '-i'
        elif val2 == 'k':
            return '-1'

    elif val1 == '-1':
        if val2 == '1':
            return '-1'
        elif val2 == 'i':
            return '-i'
        elif val2 == 'j':
            return '-j'
        elif val2 == 'k':
            return '-k'

    elif val1 == '-i':
        if val2 == '1':
            return '-i'
        elif val2 == 'i':
            return '1'
        elif val2 == 'j':
            return '-k'
        elif val2 == 'k':
            return 'j'
        
    elif val1 == '-j':
        if val2 == '1':
            return '-j'
        elif val2 == 'i':
            return 'k'
        elif val2 == 'j':
            return '1'
        elif val2 == 'k':
            return '-i'

    elif val1 == '-k':
        if val2 == '1':
            return '-k'
        elif val2 == 'i':
            return '-j'
        elif val2 == 'j':
            return 'i'
        elif val2 == 'k':
            return '1'

if __name__ == "__main__":
    main()
