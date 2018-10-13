# developped under python3.2
test_file_name = 'C-large'
f = open(test_file_name + '.in', 'r')
fw = open(test_file_name + '.out', 'w')
T = int(f.readline())
for case in range(1,T+1):
    #print(i)
    
    canides = []
    
    # read data  
    line = f.readline()
    line = line.split()
    line.reverse()
    N = int(line.pop())

    line = f.readline()
    candies = line.split(' ')
    for idx_candy in range(0, N):
        candies[idx_candy] = int(candies[idx_candy])

    # end read data

    # data process
    ans = 0
    for idx_candy in range(0, N):
        ans ^= candies[idx_candy]

    if( ans == 0 ):
        candies.sort(reverse=True)
        ans = sum(candies[0:-1])
        str_ans = str(ans)
    else:
        str_ans = "NO"
        
    # end data process

    # result representation

    output = 'Case #' + str(case) +': ' + str_ans
    print(output)

    fw.write(output + '\n')

    # end result representation

f.close()
fw.close()
