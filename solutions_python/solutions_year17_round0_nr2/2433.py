import sys
#num to list reverse
def num_to_list(num):
    num_lst_rev = []
    while num>0:
        num_lst_rev.append(num%10)
        num=num/10
    return num_lst_rev

def last_tidy_num(num):
    num_list = num_to_list(num)
    print num_list
    size_num=len(num_list)
    tidy_num=0
    mul=1
    for i in xrange(size_num):

        if len(num_list)==1:
            print 'yuvraj'
            print tidy_num
            print mul
            tidy_num=tidy_num+num_list[0]*mul
            return tidy_num

        if num_list[0]<num_list[1]:
            tidy_num=0
            mul1=1
            for j in xrange(i+1):
                tidy_num=tidy_num+9*mul1
                mul1=mul1*10
            num_list[1]=num_list[1]-1
        else:
            tidy_num = tidy_num+num_list[0]*mul
        num_list=num_list[1:]
        mul=mul*10
        print num_list
        print tidy_num
    return tidy_num

with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
    T=int(fin.readline())
    for i in xrange(T):
        N=int(fin.readline())
        fout.write('Case #'+str(i+1)+': '+str(last_tidy_num(N))+'\n')
