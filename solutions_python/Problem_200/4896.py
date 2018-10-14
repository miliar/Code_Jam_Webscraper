def check_tidy(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

#test_case = int(input())
files = open('b.in')
test_case = int(files.readline())
outp = open('b.out', 'w+')
for i in range(test_case):
    #n = int(input())
    n = int(files.readline())
    is_tidy = False
    while True:
        is_tidy = check_tidy(n)
        if is_tidy:
            break
        n -= 1
    outp.write('Case #'+str(i+1)+': '+str(n)+'\n')
    #print('Case #'+str(i+1)+': '+str(n))
outp.close()
