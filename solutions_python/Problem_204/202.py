import gcj
import itertools, math

def feasible2(q1, i1, q2, i2):
    b1 = math.floor(q1 / (0.9 * i1))
    a1 = math.ceil(q1 / (1.1 * i1))
    
    b2 = math.floor(q2 / (0.9 * i2))
    a2 = math.ceil(q2 / (1.1 * i2))

    #print(a1, b1, a2, b2)

    if a1 <= b1 and a2 <= b2 and ((b1 >= a2 and a1 <= b2) or (b2 >= a1 and a2 <= b1)):
        return True

    return False


def feasible(i, q):
    b1 = math.floor(q / (0.9 * i))
    a1 = math.ceil(q / (1.1 * i))

    return a1 <= b1



#gcj.set_sample()

ifile, ofile = gcj.get_files('B')

T = int(ifile.readline().strip())
for t in range(T):
    (N, P) = list(map(int, ifile.readline().strip().split()))
    I = list(map(int, ifile.readline().strip().split()))
    Q = []
    for i in range(N):
        Q.append(list(map(int, ifile.readline().strip().split())))


    if N == 1:
        kits = 0
        for q in Q[0]:
            if feasible(I[0], q):
                #print("Feasible", I[0], q)
                kits += 1
        ans = kits
    else:
        ans = 0
        for perm in itertools.permutations(range(P)):
            kits = 0
            #print("Check", perm)
            for i in range(P):
                f = feasible2(Q[0][i], I[0], Q[1][perm[i]], I[1])
                if f:
                    #print(Q[0][i], I[0], Q[1][perm[i]], I[1], f)
                    kits += 1
            #print(perm, kits)
            ans = max(ans, kits)


    gcj.print_answer(ofile, t, ans)