
def fill9(num, start):
    for i in range(start, len(num)):
        num[i] = '9'

t = int(raw_input())  # read a line with a single integer
for task in xrange(1, t + 1):
    num_str = list(raw_input())
    for i in range(len(num_str) - 1, 0, -1):
        if int(num_str[i]) < int(num_str[i - 1]):
            num_str[i - 1] = str(int(num_str[i - 1]) - 1)
            fill9(num_str, i)
    if num_str[0] == "0":
        num_str = num_str[1:]
    print "Case #{}: ".format(task) + "".join(num_str)



