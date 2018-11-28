#!/bin/env python3

T=0
test_case_no = 1
M=0
N=0
line_no=0

f = open("result_large.txt", "w")

for line in open("./B-large.in"):
    if T == 0:
        T = int(line)

    else:
        if line_no == N:
            line_no = 0
            pre_line = []
            tmp = []
            b = line.split()
            N=int(b[0])
            M=int(b[1])
            not_possible = False
            print("{0}, {1}".format(N,M))
        
        else:
            diff_point = []
            tmp.append([int(x) for x in line.split()])

            line_no += 1

        if line_no == N:
            for i in range(0,N):
#                diff_point.append([cnt for cnt, item in enumerate(tmp[i]) if item != max(tmp[i])])

                for cnt, item in enumerate(tmp[i]):
                    if item != max(tmp[i]):
                        diff_point.append((i, cnt))

#            print(diff_point)
            for x in diff_point:
                tmp_a = []
                for j in range(0,N):
#                    print("j, x[1]: {0}, {1}".format(j, x[1]))
#                    print(tmp[j][x[1]])
                    tmp_a.append(tmp[j][x[1]])
                
#                print(tmp_a)
#                print("tmp[x[0]][x[1]], max_tmp_a : {0}, {1}".format(tmp[x[0]][x[1]], max(tmp_a)))

                if tmp[x[0]][x[1]] != max(tmp_a):
                    not_possible = True
#                    print("NG")
#                else:
#                    print("OK")

            print(test_case_no)
            print(tmp)
#            print(diff_point)
            if not_possible:
                print("NO")
                f.write("Case #{0}: NO\n".format(test_case_no))
            else:
                print("YES")
                f.write("Case #{0}: YES\n".format(test_case_no))

            test_case_no += 1

f.close()
