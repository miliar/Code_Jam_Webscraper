import sys

name = "B-small-attempt0"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input()
    N, R, O, Y, G, B, V = line.split()

    N = int(N)
    R = int(R)
    O = int(O)
    Y = int(Y)
    G = int(G)
    B = int(B)
    V = int(V)
    #print R, O, Y, G, B, V

    n = N
    if V > N/2:
        print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
        continue
    elif V == N/2:
        if Y < N-V:
            print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
            continue
        else:
            print("Case #" + str(testCase) + ": " + ''.join(['YV']*V) + 'Y'*(Y-V))
            continue
    else:
        n = n - 2*V - 1 + 1
        Y = Y-V

    if G > N / 2:
        print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
        continue
    elif G == N / 2:
        if R < N - G:
            print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
            continue
        else:
            print("Case #" + str(testCase) + ": " + ''.join(['RG'] * G) + 'R'*(R-G))
            continue
    else:
        n = n - 2 * G - 1 + 1
        R = R - G

    if O > N / 2:
        print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
        continue
    elif O == N / 2:
        if B < N - O:
            print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
            continue
        else:
            print("Case #" + str(testCase) + ": " + ''.join(['BO'] * G) + 'B' * (B - O))
            continue
    else:
        n = n - 2 * O - 1 + 1
        B = B - O

    if n % 2 == 1:
        maximum_num_each_color = (n + 1) / 2
    else:
        maximum_num_each_color = n / 2 + 1

    if R >= maximum_num_each_color or Y >= maximum_num_each_color or B >= maximum_num_each_color:
        print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
        continue
    else:
        res =['']*n
        i = 0
        current_pos = 0
        while(i<3):
            m = max([R,B,Y])
            index = [R,B,Y].index(m)
            if index == 0:
                now = "R"
                R -= m
            elif index == 1:
                now = "B"
                B -= m
            else:
                now = "Y"
                Y -= m
            i+=1
            j = 0
            while(j<m):
                j += 1
                while(res[current_pos]!=''):
                    current_pos = (current_pos+1)%n
                res[current_pos] = now
                current_pos = (current_pos + 2)%n

    if V != 0:
        r = res.index('Y')
        res[r] = 'YV'*V + 'Y'

    if G != 0:
        r = res.index('R')
        res[r] = 'RG' * G +'R'

    if O != 0:
        r = res.index('B')
        res[r] = 'BO' * O + 'B'

    print("Case #" + str(testCase) + ": " + ''.join(res))














