'''
@author: Shawn McClelland
'''

###  Enter filename for input and output
filename = 'A-test'
filename = 'A-small-attempt2'
filename = 'A-large'

file_in = open('%s.in' % filename)

####  Get first line of file as number of cases
number_cases = int(file_in.readline())

####  Get lists of data for each Case - 3 places to remove '#'
#dataline_single_integer1 = []
#dataline_single_integer2 = []
dataline_single_string1 = []
#dataline_multiple_integers1 = []
#dataline_multiple_integers2 = []
#dataline_multiple_strings1 = []


for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
#    dataline_single_integer1.append(int(file_in.readline()))
#    dataline_single_integer2.append(int(file_in.readline()))
    dataline_single_string1.append(file_in.readline())
#    dataline_multiple_integers1.append(map(int, file_in.readline().split()))
#    dataline_multiple_integers2.append(map(int, file_in.readline().split()))
#    dataline_multiple_strings1.append(file_in.readline().split())
    

file_in.close()
file_out = open('%s.out' % filename, 'w')


###  Iterate for each case
for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
#    tmp_datas1 = dataline_single_integer1[i]
#    tmp_datas2 = dataline_single_integer2[i]

    tmp_datass1 = dataline_single_string1[i]   
    if tmp_datass1 == '\n': tmp_datass1 = tmp_datass1[:-1]

#    tmp_datam1 = dataline_multiple_integers1[i]
#    tmp_datam2 = dataline_multiple_integers2[i]
#    tmp_datams1 = dataline_multiple_strings1[i]



###  Algorithm Start
    tmp_datass1 = tmp_datass1.split()
    N = int(tmp_datass1.pop(0))
    R = []
    P = []
    counter=0
    for j in tmp_datass1:
        if counter == 0:
            R.append(j)
            counter += 1
        else:
            P.append(int(j))
            counter = 0
    print R, P
    total = 0
    Ocounter, Bcounter = 0, 0
    Ospot,Bspot = 1,1
    lastmove = 'O'
    for j in xrange(N):
        if lastmove == R[j]:
            if R[j] == 'O':
                move = abs(Ospot-P[j])
                Ospot = P[j]
                total += move+1
                Ocounter += move+1
                lastmove = 'O'
                print 'lOc', Ocounter
            if R[j] == 'B':
                move = abs(Bspot-P[j])
                Bspot = P[j]
                total += move+1
                Bcounter += move+1
                lastmove = 'B'
                print 'lBc', Bcounter
        else:
            if R[j] == 'O':
                Ocounter = 0
                move = abs(Ospot-P[j])
                if move > Bcounter:
                    move = move - Bcounter
                    Bcounter = 0
                else:
                    move = 0
                Ospot = P[j]
                total += move+1
                Ocounter += move+1
                lastmove = 'O'
                print 'Oc', Ocounter
            if R[j] == 'B':
                Bcounter = 0
                move = abs(Bspot-P[j])
                if move > Ocounter:
                    move = move - Ocounter
                    Ocounter = 0
                else:
                    move = 0
                Bspot = P[j]
                total += move+1
                Bcounter += move+1
                lastmove = 'B'
                print 'Bc', Bcounter
        print '*', total
    print 'TOTAL', total
        
        
    output1 = total
    
    
        
    linein = str("Case #%d:" % (i + 1)) + str(' ') + str(output1) + str('\n')
    file_out.write(linein)

###  Algorithm End



file_out.close()