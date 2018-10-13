import math
result_list = [0, 1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001]
result_set = set()
for number in result_list:
    result_set.add(number ** 2)

total = input()

for index in range(total):
    count = 0
    min_number, max_number = map(int, raw_input().split())
    for number in xrange(min_number, max_number+1):
        if number in result_set:
            count += 1
    result = "Case #%s: %s" % (index+1, count)
    print result
