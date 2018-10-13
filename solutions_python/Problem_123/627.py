__author__ = 'jeff'

from collections import deque

base = "A-small-attempt2"
#base = "A1_test"

f = open(base+'.in','r')
fout = open(base+'.out','w')

t = int(f.readline())

def proc( a, motes):
    while( len( motes ) and motes[0] < a ):
        a += motes.popleft()
    return a


max_lev = 100000

for case in range(1,t+1):
    [a,n] = f.readline().split(' ')
    a=int(a)
    n=int(n)
    motes = list(map( int, f.readline()[0:-1].split(' ')))
    motes.sort()
    print(a,motes)
    motes = deque( motes )


    moves = 0
    adds = removes = 0
    lev_count = 0
    while( len( motes) ):

        a=proc(a,motes)

        if( not len( motes ) ):
            break

        a_copy = a
        these_adds = 0
        while( a>1 and a_copy <= motes[0] ):
            these_adds += 1
            a_copy += (a_copy - 1)

        if( these_adds > 0 and these_adds < len( motes )):
            adds += these_adds
            a = a_copy
        else:
            removes += len( motes )
            motes = deque([])
    moves = moves + adds + removes
    out_s = 'Case #{0}: {1}\n'.format(case,moves)
    print( out_s )
    fout.write(out_s)

f.close()
fout.close()





