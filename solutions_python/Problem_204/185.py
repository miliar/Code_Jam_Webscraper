# Python 3.5

import math

def main():
    problem = open("B-large.in", "r")
    output = open("B-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        N = int(line[0])
        P = int(line[1])
        line = problem.readline().strip().split()
        R = [int(a) for a in line]
        Q = []
        for i in range(N):
            line = problem.readline().strip().split()
            Q.append(sorted([int(a) for a in line]))
            
        min_req = 1000001
        for i in range(N):
            if min_req > R[i]:
                min_req = R[i]
                min_ing = i

        packages = 0
        while Q[min_ing] != []:
            curr = Q[min_ing].pop(0)
            servings_lower = math.ceil(curr / (1.1 * R[min_ing]))
            servings_upper = math.floor(curr / (0.9 * R[min_ing]))
            for serving in range(servings_lower, servings_upper+1):
                possible_set = []
                for i in range(N):
                    if i == min_ing:
                        possible_set.append(0)
                        continue
                    need = serving * R[i]
                    min_val = 1000001
                    min_idx = -1
                    for pack in range(len(Q[i])):
                        if need * 0.9 <= Q[i][pack] and Q[i][pack] <= need * 1.1:
                            if Q[i][pack] < min_val:
                                min_val = Q[i][pack]
                                min_idx = pack
                    if min_idx >= 0:
                        possible_set.append(min_idx)
                if len(possible_set) == N:
                    for i in range(N):
                        if i == min_ing: continue
                        Q[i].pop(possible_set[i])
                    packages += 1
                    break
        output.write("Case #" + str(test+1) + ":")
        output.write(" " + str(packages) + "\n")
    problem.close()
    output.close()

main()
