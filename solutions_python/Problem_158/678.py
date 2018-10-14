res = {1:{1:[1], 2:[1,2], 3:[1], 4:[1,2]},
       2:{2:[1,2], 3:[1,2,3], 4:[1,2]},
       3:{3:[1,3], 4:[1,2,3,4]},
       4:{4:[1,2,4]}}

f = open('D-small-attempt2.in', 'r')
out = open('out.txt', 'w')
T = int(f.readline())

for case in range(T):
    line = f.readline()
    pattern = line.strip().split()
    X = int(pattern[0])
    R = int(pattern[1])
    C = int(pattern[2])

    if C < R:
        t = R
        R = C
        C = t

    print(R, C, X)
    if X in res[R][C]:
        out.write("Case #" + str(case + 1) + ": GABRIEL\n")
    else:
        out.write("Case #" + str(case + 1) + ": RICHARD\n")




