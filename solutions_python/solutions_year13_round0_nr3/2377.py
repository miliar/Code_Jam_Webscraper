from math import sqrt
input_file = open('/Users/arisha/Desktop/programming/Python/codejam/2013/fair_square/C-small-attempt0.in')
output_file = open('/Users/arisha/Desktop/programming/Python/codejam/2013/fair_square/output.out', 'w')
T = int(input_file.readline())

for i in range(T):
    a, b = map(int, input_file.readline().strip().split())
    count = 0
    for num in range(a, b+1):
        str_num = str(num)
        if str_num != str_num[::-1]:
            continue
        
        sqrtd = sqrt(float(num))
        #print sqrtd == int(sqrtd), "test b", num
        if sqrtd != int(sqrtd):
            continue
        
        str_sqrt = str(int(sqrtd))
        #print str_sqrt == str_sqrt[::-1], "test c", num
        if str_sqrt != str_sqrt[::-1]:
            continue
        count += 1

    ans = "Case #%d: %d\n" %(i+1, count)
    print ans
    output_file.write(ans)

input_file.close()
output_file.close()
