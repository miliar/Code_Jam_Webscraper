__author__ = 'Mariyan Stoyanov'

of = open('B-large.out', 'w')

f = open('B-large.in', 'r')

counter = 0

number_of_test_cases = 0
row = 0

test_cases = []
lawns_list = []

readNM = False
count_n = 0

my_lawn = []


for line in f:
    if counter==0:
        number_of_test_cases = int(line)
        readNM = True
    else:
        if readNM:
            if len(my_lawn)>0:
                lawns_list.append(tuple(my_lawn))
            my_lawn = []
            N,M = map(int,line.rstrip('\n').split())
            readNM = False
            count_n = 0
        else:
            count_n += 1
            if count_n==N:
                readNM = True
            my_lawn.append(map(int,line.rstrip('\n').split()))

    counter += 1

if len(my_lawn)>0:
    lawns_list.append(my_lawn)

if(len(lawns_list)!=number_of_test_cases):
    raise ValueError('number of test cases read from file does not match the indicated number of test cases that should be there')

f.close()



for case_num in range(len(lawns_list)):
    lawn = lawns_list[case_num]
    possible = True

    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            col = [lawn[i1][j] for i1 in range(len(lawn))]
            maxj = max(lawn[i])
            maxi = max(col)

            if maxi>lawn[i][j] and maxj>lawn[i][j]:
                possible = False
                break

    if possible:
        print 'Case #%d: YES'%(case_num+1)
        of.write('Case #%d: YES'%(case_num+1))
    else:
        print 'Case #%d: NO'%(case_num+1)
        of.write('Case #%d: NO'%(case_num+1))

    of.write('\n')
of.close()
