times = int(raw_input())
i = 1
process = []
while i <= times:
    result_set = set()
    min_str, max_str = raw_input().split()
    min_num, max_num = int(min_str), int(max_str)
    bound = (max_num + min_num) / 2
    first = min_num
    while first <= max_num:
        first_str = str(first)
        for k in range(len(first_str)):
            temp_str = first_str[k:] + first_str[:k]
            if min_num <= int(temp_str) <= max_num and temp_str != first_str and temp_str[0] != '0':
                result_set.add((first_str, temp_str))
                result_set.add((temp_str, first_str))
        first += 1

    process.append("Case #%d: %d" % (i, len(result_set)/2))
    i += 1

for j in process:
    print j

