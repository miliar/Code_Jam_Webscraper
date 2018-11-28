with open('C-small-attempt0.in','r') as reading,open('Solution C_very small.txt','w') as writing:
    no_of_testcase = int(reading.readline())

    for i in range(1,no_of_testcase+1):
        a, b = reading.readline().split()
        a, b = int(a), int(b)
        upper = int(b**0.5) + 1
        if int(a**0.5)**2 == a:
            lower = int(a**0.5)
        else:
            lower = int(a**0.5) + 1
        count = 0
        for num in range(lower,upper):
            str_num = str(num)
            if str_num == str_num[::-1]:
                num_2 = num**2
                str_num_2 = str(num_2)
                if str_num_2 == str_num_2[::-1]:
                    count += 1
        writing.write('Case #%d: %d\n'%(i, count))