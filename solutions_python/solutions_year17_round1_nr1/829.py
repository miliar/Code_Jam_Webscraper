# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.

# This is all you need for most Google Code Jam problems.
import random
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    a  = []
    need_array = [0]*m
    need_mat = []
    skipped_line =[]
    for j in xrange(n):
        strin = list(raw_input())
        a.append(strin)
        need_mat.append(need_array)

    for j in xrange(n):
        flag = 0
        flag_forward = 0
        for k in xrange(m):
            if a[j][k] != "?":
                s = k-1
                while(s >= 0 and a[j][s] =="?"):
                    a[j][s] = a[j][k]
                    s -= 1
                s = k+1
                while(s < m and a[j][s] == "?"):
                    a[j][s] = a[j][k]
                    s += 1
                    flag_forward = 1
                flag = 1
            if flag_forward == 1:
                k = s - 1
        if flag == 0:
            skipped_line.append(j)

    while(skipped_line):
        num = skipped_line.pop()
        for j in xrange(m):
            if num == n-1:
                if a[num-1][j] != "?":
                    a[num][j] = a[num-1][j]
                else:
                    skipped_line.insert(0,num)
            else:
                if a[num+1][j] != "?":
                    a[num][j] = a[num+1][j]
                else:
                    while num -1 >=0 :
                        if a[num-1][j] != "?":
                            a[num][j] = a[num-1][j]
                            break
                        else:
                            skipped_line.insert(0,num)
                        num -= 1
    print "Case #{}:".format(i)

    for j in xrange(n):
        moji = "".join(a[j])
        print "{}".format(moji)



  # check out .format's specification for more formatting options
