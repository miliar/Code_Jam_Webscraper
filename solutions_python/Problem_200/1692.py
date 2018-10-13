import sys

last_number = 0
sys.setrecursionlimit(2000)



def tidy_num(num_ls,i):
    if i <= 0:
        return num_ls
    if num_ls[i]<num_ls[i-1]:
        for j in range(i,len(num_ls)):
            num_ls[j] = 9
        num_ls[i-1] -= 1
    return tidy_num(num_ls,i-1)


input = open('gs2.txt', 'r')
tests = int(input.readline())
# print (tests)
for i in range(1,tests+1):
    test = input.readline()
    num = list(str(int(test)))
    for j in range(0,len(num)):
        num[j] = int(num[j])
    # fill_index()
    # last_number = 0
    # check_flips(s,k)
    result = int(''.join(str(x) for x in tidy_num(num,len(num)-1)))
    print ('Case #%s:'%i,result)
