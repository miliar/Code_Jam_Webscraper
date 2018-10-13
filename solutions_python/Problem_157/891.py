import fileinput as FI

ref =  {'1': {'1':'1','i': 'i','j': 'j','k': 'k', '-1':'-1','-i': '-i','-j':'-j','-k':'-k'},
            'i': {'1':'i','i': '-1','j': 'k','k':'-j', '-1':'-i','-i':'--1','-j':'-k','-k':'--j'},
            'j': {'1':'j','i': '-k','j': '-1','k':'i', '-1':'-j','-i':'--k','-j':'--1','-k':'-i'},
            'k': {'1':'k','i': 'j','j': '-i','k':'-1', '-1':'-k','-i':'-j','-j':'--i','-k':'--1'},
             '-1': {'1':'-1','i': '-i','j': '-j','k': '-k', '-1':'1','-i': 'i','-j':'j','-k':'k'},
            '-i': {'1':'-i','i': '1','j': '-k','k':'j', '-1':'i','-i':'-1','-j':'k','-k':'-j'},
            '-j': {'1':'-j','i': 'k','j': '1','k':'-i', '-1':'j','-i':'-k','-j':'-1','-k':'i'},
            '-k': {'1':'-k','i': '-j','j': 'i','k':'1', '-1':'k','-i':'j','-j':'-i','-k':'-1'}
            }

def quartMul(mistake, v, index):
    mul = '1'
    test = []
    for i in xrange(index, len(mistake)):
        mul = ref[mul][mistake[i]]
        if mul == v:
            test.append(i)
    if test == []:
        return []
    else:
        return test 

def findI(mistake,index):
    return quartMul(mistake,'i',index)
    
def findJ(mistake, index):
    return quartMul(mistake,'j', index)
def findK(mistake, index):
    return quartMul(mistake,'k', index)

def isCorrect(mistake):
    p = []
    q = []
    r = []
    testValue=len(mistake)-1
    p = findI(mistake, 0)
    for x in p:
        q.append(findJ(mistake, x+1))
    #else: return 'NO'
    q = [item for sublist in q for item in sublist]
    q = list(set(q))        
    for x in q:
        r.append(findK(mistake, x+1))
    r = [item for sublist in r for item in sublist]
    r = list(set(r))
    if testValue in r:
        return 'YES'
#                else: continue
    return 'NO'
       
def main():
    inPut = FI.input()
    cases = int(inPut.readline())

    for case in xrange(cases):
        
    # associative law holds but commutative law does not /// negatives work same as maths.
        [L,X] = [int(x) for x in inPut.readline().split()]
        mistake = inPut.readline().strip()
        if L*X<2 or L==1:
            y= 'NO'
        else:
            y = isCorrect(mistake)
            if y== 'YES' and X%2 != 0 :
                y='YES'
            elif X!=1:
                mistake = mistake * X
                y = isCorrect(mistake)
        print 'Case #'+ str(case+1) + ': '+ str(y)
if __name__ == "__main__":
    main()