t = int(input())  # read a line with a single integer
filep = open("p2.txt", 'w')
for i in range(1, t + 1):
    n = int(input())  # read a list of integers, 2 in this case
    for num in range(n,0,-1):
        num_string = str(num)
        pre = int(num_string[0])
        for ch in num_string:
            if int(ch) >= pre:
                tidy = True
                pre = int(ch)
            else:
                tidy = False
                break
        if tidy:
            filep.write("Case #{}: {}\n".format(i, num))
            break
    # check out .format's specification for more formatting options
filep.close()
