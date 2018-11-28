def read_file():
    f = open("B-large.in", 'r')
    num_case = int(f.readline())

    for n in range(num_case):
        flag = False
        num = int(f.readline())
        
        while(not flag):
            num_set = map(int, list(str(num)))
            if sorted(num_set) == num_set:
                flag = True
            else:
                num = adjust_num(num_set)
            
        print_result(n, num)

def print_result(case, max_num):
    print('Case #{}: {}'.format(case+1,max_num))    
    
def adjust_num(num):
    n = len(num)
    for i in xrange(1,n):
        if num[n-i] < num[n-i-1]:
            num[n-i] = 9
            for j in xrange(1,i):
                num[n-j] = 9
            num[n-i-1] = num[n-i-1]-1

    return int(''.join(map(str,num)))

read_file()