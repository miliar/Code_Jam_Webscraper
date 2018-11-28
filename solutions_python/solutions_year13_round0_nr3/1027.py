__author__ = 'Mariyan Stoyanov'

from math import sqrt

def palindromSqrt(A,B):
    eleven = [1,1]
    twelve = [2,2]

    #s = set(map(str,[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]))
    s = set()
    for i in range(len(str(int(A))), len(str(int(B)))+1):
        if i==1:
            if A<=1 and 1<=B:
                s.add('1')
            if A<=2 and 2<=B:
                s.add('2')
            if A<=3 and 3<=B:
                s.add('3')
        if i==2:
            if A<=11 and 11<=B:
                s.add('11')
            if A<=22 and 22<=B:
                s.add('22')
        if i>2:
            if i%2==0:
                num = str(eleven[0])+'0'*(i-2)+str(eleven[1])
                num_i = int(num)
                if A<=num_i and num_i<=B:
                    s.add(num)
                num = str(eleven[0])+'1'*(i-2)+str(eleven[1])
                num_i = int(num)
                if A<=num_i and num_i<=B:
                    s.add(num)
                num = str(twelve[0])+'0'*(i-2)+str(twelve[1])
                num_i = int(num)
                if A<=num_i and num_i<=B:
                    s.add(num)
            else:
                a = str(eleven[0])+'0'*(i-2)+str(eleven[1])
                b = str(eleven[0])+'1'*(i-2)+str(eleven[1])

                num = int(a)
                if A<=num and num<=B:
                    s.add(a)
                num = int(b)
                if A<=num and num<=B:
                    s.add(b)

                for c in [0,1,2]:
                    if c!=0:
                        l = list(a)
                        l[i/2]=str(c)
                        num = ''.join(l)
                        num_i = int(num)
                        if A<=num_i and num_i<=B:
                            s.add(num)
                    if c!=1:
                        l = list(b)
                        l[i/2]=str(c)
                        num = ''.join(l)
                        num_i = int(num)
                        if A<=num_i and num_i<=B:
                            s.add(num)

                a2 = str(twelve[0])+'0'*(i-2)+str(twelve[1])
                num = int(a2)
                if A<=num and num<=B:
                    s.add(a2)

                l = list(a2)
                l[i/2]=str(1)
                num = ''.join(l)
                num_i = int(num)
                if A<=num_i and num_i<=B:
                    s.add(num)

    return s

of = open('C-small-attempt0.out', 'w')

f = open('C-small-attempt0.in', 'r')

counter = 0

number_of_test_cases = 0
row = 0

test_cases = []
ranges_list = []



for line in f:
    if counter==0:
        number_of_test_cases = int(line)
    else:
        ranges_list.append(tuple(line.rstrip('\n').split()))

    counter += 1

#print len(ranges_list)
if(len(ranges_list)!=number_of_test_cases):
    raise ValueError('number of test cases read from file does not match the indicated number of test cases that should be there')

f.close()

for case_num in range(len(ranges_list)):
    A,B = map(int,ranges_list[case_num])
    #print A,B
    A_sqrt = sqrt(A)
    B_sqrt = sqrt(B)

    s = palindromSqrt(A_sqrt,B_sqrt)

    print 'Case #%d: %d'%(case_num+1, len(s))
    of.write('Case #%d: %d'%(case_num+1, len(s)))
    '''
    ls = list(map(int,s))
    l = sorted(map(int,ls))
    for p in l:
        print p, int(p)*int(p)
    '''

    of.write('\n')
of.close()

 

 