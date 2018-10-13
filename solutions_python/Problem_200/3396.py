T = int(raw_input())

for i in range(1, T+1):
    print 'Case #%d:' % i,

    num = raw_input()
    num_list = [int(e) for e in num]
    num_len = len(num)

    flag = 0
    if sorted(num_list) == num_list:
        print num
        continue
        
    for e in range(num_len-2, -1, -1):
        if num_list[e+1] >= num_list[e]:
            continue
        else:
            num_list[e] = num_list[e]-1
            for j in range(e+1, num_len):
                num_list[j] = 9
    solution = ''
    for j in num_list:
        solution += str(j)

    print int(solution)

    
