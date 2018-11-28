# import copy

# print l

t = int(raw_input())
# read a line with a single integer
for j in xrange(1, t + 1):
    string, k = raw_input().split()
    k = int(k)

    # string = raw_input()
    l = [1 if item == "+" else 0 for item in string]
    # print l
    # op_num = 0
    operations = []
    operation_index = 0
    # g = copy.deepcopy(l)
    for i in xrange(len(string) - k + 1):
        while operation_index < len(operations) and \
                                i - operations[operation_index] >= k:
            operation_index += 1

        if l[i] + (len(operations) - operation_index) % 2 == 1:
            pass
        else:
            operations.append(i)

            # for h in xrange(k):
            #     g[i + h] += 1
            #     g[i + h] %= 2
        # print i, operation_index, operations, operations[operation_index:]
        # print l
        # print g
        # print "--"

    flag = True

    for i in xrange(len(string) - k, len(string)):
        while operation_index < len(operations) and \
                                i - operations[operation_index] >= k:
            operation_index += 1

        if l[i] + (len(operations) - operation_index) % 2 == 1:
            pass
        else:
            flag = False
            break

    if flag is False:
        ans = "IMPOSSIBLE"
    else:
        ans = len(operations)#, operations

    print "Case #{}: {}".format(j, ans)

#+-+-+-+-+-++++++