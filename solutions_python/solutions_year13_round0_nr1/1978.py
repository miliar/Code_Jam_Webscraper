'''
Created on Apr 13, 2013

@author: friend1
'''


def solve(all):
    
    r1 ='' 
    r2= ''
    r3 = ''
    r4 =''
    j = 1
    for x in all:
            r1 += x[0]
            r3 += x[1]
            r2 += x[2]
            r4 += x[3] 
            if ( x == 'XXXX' or (x.count('T') + x.count('X') == 4 )):
                return 'X won'
            elif (x == 'OOOO'or (x.count('T') + x.count('O') == 4 )):
                return 'O won'
    if ( r1 == 'XXXX' or r2 == 'XXXX' or r3 == 'XXXX'or r4 == 'XXXX' or (r1.count ('T') + r1.count('X') == 4 )or (r2.count ('T') + r2.count('X') == 4 )or (r3.count ('T') + r3.count('X') == 4 )or (r4.count ('T') + r4.count('X') == 4)):
                return 'X won'
    elif (r1 == 'OOOO' or r2 == 'OOOO' or r3 == 'OOOO' or r4 == 'OOOO' or (r1.count ('T') + r1.count('O') == 4 )or (r2.count ('T') + r2.count('O') == 4  )or (r3.count ('T') + r3.count('O') == 4  )or (r4.count ('T') + r4.count('O') == 4 )):
                return 'O won'
    a = ''
    b =  ''
    ti = 0
    for x in all:
        a += x[ti]
        b += x[-1*(ti +1)]
        ti +=1
    
    #print a + '\n'
    #print b+ '\n'
    if ( a == 'XXXX' or (a.count('T') + a.count('X') == 4 )or  b == 'XXXX' or (b.count('T') + b.count('X') == 4 )):
                return 'X won'
    elif (a == 'OOOO'or (a.count('T') + a.count('O') == 4 ) or b == 'OOOO'or ( b.count('T') + b.count('O') == 4 )):
                return 'O won'
    for x in all:
            if( x.find('.') != -1):
                return 'Game has not completed'    
        
    return 'Draw'
    
try:
    fin = open(r'in\A-large.in','r')
    fout = open(r'A-large.out','w')

    amount = int(fin.readline())
    
    for i in range(1,amount+1):
        
        ex1 = []
        
        for x in xrange(4):
            ex1.append(fin.readline().rstrip('\n'))
       
        fin.readline()
       
       
        fout.writelines('Case #'+str(i)+': '+ solve(ex1 )+'\n')
        
        
finally:
    fin.close()
    fout.close()        
            