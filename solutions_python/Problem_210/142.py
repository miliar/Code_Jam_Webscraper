from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    A_C,A_J = map(int, stdin.readline().strip().split())
    C = [tuple(map(int, stdin.readline().strip().split())) for i in range(A_C)]
    J = [tuple(map(int, stdin.readline().strip().split())) for i in range(A_J)]

    if A_C == 1 or A_J == 1:
        stdout.write("Case #{:d}: 2\n".format(case_num))
    else:
        X = C if A_C > 0 else J
        if len(X) == 1:
            n = 1
        else: # len(X) == 2
            if X[0][1] == X[1][0] or X[1][1] == X[0][0]:
                n = 1
            else:   
                n = 2
        if n == 1:
            stdout.write("Case #{:d}: 2\n".format(case_num))
        else:
            X.sort(key=lambda x:x[0])
            if X[1][1]-X[0][0] <= 720 or 1440-(X[1][0]-X[0][1]) <= 720:
                stdout.write("Case #{:d}: 2\n".format(case_num))
            else:
                stdout.write("Case #{:d}: 4\n".format(case_num))
            

    # stdout.write("Case #{:d}: {:f}\n".format(case_num, total))
