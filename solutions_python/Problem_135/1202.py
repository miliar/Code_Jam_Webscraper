#from mpmath import *
#from bigfloat import *
def compare_lists(a,b):
    print a
    print b
    matched_numbers = []
    for i in a:
        for j in b:
            if i==j:
                matched_numbers.append(i)
    print matched_numbers
    return matched_numbers
f = open('A-small-attempt0.in', 'r')
num=int(f.readline())
output=open('result','w')
case=0
while num!=0:
    num-=1
    case+=1
    row = int(f.readline())
    result_line_1 = []
    for i in xrange(1,5):
        line=[int(x) for x in f.readline().split()]
        if i == row:
            result_line_1=line
    row = int(f.readline())
    result_line_2 = []
    for i in xrange(1,5):
        line=[int(x) for x in f.readline().split()]
        if i == row:
            result_line_2=line
    ret_num = compare_lists(result_line_2,result_line_1)
    if len(ret_num)>1:
        print('Case #'+str(case)+': '+'Bad magician!')
        output.write('Case #'+str(case)+': '+'Bad magician!\n')
    elif len(ret_num)==1:
        print('Case #'+str(case)+': '+str(ret_num[0]))
        output.write('Case #'+str(case)+': '+str(ret_num[0])+'\n')
    elif len(ret_num)==0:
        print('Case #'+str(case)+': '+'Volunteer cheated!')
        output.write('Case #'+str(case)+': '+'Volunteer cheated!\n')
output.close()
