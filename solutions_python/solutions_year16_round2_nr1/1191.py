test_cases = int(raw_input())
def printNumber(word,test):
    E=word.count('E')
    G=word.count('G')
    F=word.count('F')
    I=word.count('I')
    H=word.count('H')
    O=word.count('O')
    N=word.count('N')
    S=word.count('S')
    R=word.count('R')
    U=word.count('U')
    T=word.count('T')
    W=word.count('W')
    V=word.count('V')
    X=word.count('X')
    Z=word.count('Z')
    zeros=Z
    if(zeros>0):
        E=E-zeros
        R=R-zeros
        O=O-zeros
    eights=G
    if(eights>0):
        E=E-eights
        I=I-eights
        H=H-eights
        T=T-eights
    two=W
    if(two>0):
        T=T-two
        O=O-two
    four=U
    if(four>0):
        O=O-four
        F=F-four
        R=R-four
    six=X
    if(six>0):
        S=S-six
        I=I-six
    ones=O
    fives=F
    nines=I
    threes=T
    sevens=S
    if(fives>0):
        nines=nines-fives
    result='0'*zeros+'1'*ones+'2'*two+'3'*threes+'4'*four+'5'*fives+'6'*six+'7'*sevens+'8'*eights+'9'*nines
    print "Case #"+str(test+1)+": "+result

for test in range(test_cases):
    word = (raw_input())
    printNumber(word,test)