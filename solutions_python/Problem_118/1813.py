from math import sqrt

fair_square = []

def is_fair(n):
    aux = n
    rev = 0

    while(aux > 0):
        rev = rev*10 + (aux % 10);
        aux = aux/10;

    return rev == n;

def is_square(n):
    a = sqrt(n);
    if ( a-int(sqrt(n)) > 0 or a-int(sqrt(n)) < 0 ):
        return 0
    return is_fair(int(sqrt(n)));

def genEvenPalindromes(l, fl):

    if( l == 0 ):
        return [ '','','','','','','','','','' ]


    if( l == 1 ):
        pal = [ '0','1','2','3','4','5','6','7','8','9' ]

    if( l > 1 ):
        before = genEvenPalindromes(l-2, fl)

        pal = []

        if( l==fl ):
            listi = [ '1','4' ]
        else:
            listi = [ '0','1','2','3','4','5','6','7','8','9' ]

        for i in listi:
            for j in before:
                pal.append( i+j+i )


    for i in pal:
        if( int(i) % 10 != 0 ):
            if( is_square(int(i)) ):
                fair_square.append( int(i) )

    return pal


NTCc = 0
NTC = int(input())

genEvenPalindromes(15,15)

while(NTCc < NTC):

    NTCc += 1
    counter = 0
    a,b = map(int, raw_input().split());

    for i in fair_square:
        if ( i >= a and i <= b):
            counter+=1
        elif ( i > b ):
            break

    print "Case #"+str(NTCc)+": "+str(counter)+"\n"



