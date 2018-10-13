def split(str):
    return list ( str )

def split_int(num):
    return [int(x) for x in str(num)]

def ordertest(A):
    return all(A[i] <= A[i+1] for i in xrange(len(A)-1))

test_cases = int(raw_input())
for i in xrange(0, test_cases):
    value = int(raw_input())
    if value == 1:
        print('Case #' + str(i+1) + ': ' + str(value))
    if value > 1:
        while value > 0:
            value_split = split_int(value)
            if ordertest(value_split):
                print('Case #' + str(i+1) + ': ' + str(value))
                break
            # value = value - 1
            a_list = value_split
            for x in xrange(0, len(a_list)-1):
                if a_list[x]>a_list[x+1]:
                    value_split[x] = value_split[x] - 1
                    for y in xrange(x+1, len(a_list)):
                        value_split[y] = 9
                    break
            value = int(''.join(map(str,value_split)))

