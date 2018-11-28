import sys

fin = sys.stdin
num_cases = int(fin.readline().strip())

def solve(s1, s2):
    r1 = []
    r2 = []

    for i in range(len(s1)):
        if s1[i] != "?" and s1[i] == s2[i]:
            r1.append(s1[i])
            r2.append(s2[i])
            continue
        if s1[i] != "?" and s2[i] != "?":
            r1.append(s1[i])
            r2.append(s2[i])
            s1_high = int(s1[i]) > int(s2[i])
            r1.extend(playout(s1[i+1:], '0' if s1_high else '9'))
            r2.extend(playout(s2[i+1:], '9' if s1_high else '0'))
            break

        if s1[i] == "?" and s2[i] == "?":
            min_d = 10**(len(s1)+1)
            best_n1 = []
            best_n2 = []
            for o1,o2 in [(0,0), (0,1), (1,0)]:
                n1, n2 = solve(str(o1) + s1[i+1:], str(o2) + s2[i+1:])
                d = abs(int("".join(n1)) - int("".join(n2)))
                if d < min_d:
                    min_d = d
                    best_n1 = n1
                    best_n2 = n2
            r1.extend(best_n1)
            r2.extend(best_n2)
            break

        if s1[i] == "?":
            min_t = max(0, int(s2[i])-1)
            max_t = min(9, int(s2[i])+1)
            min_d = 10**(len(s1)+1)
            best_n1 = []
            best_n2 = []

            for t in range(min_t, max_t+1):
                n1, n2 = solve(str(t) + s1[i + 1:], s2[i:])
                d = abs(int("".join(n1)) - int("".join(n2)))
                if d < min_d:
                    min_d = d
                    best_n1 = n1
                    best_n2 = n2
            r1.extend(best_n1)
            r2.extend(best_n2)
            break

        if s2[i] == "?":
            min_t = max(0, int(s1[i]) - 1)
            max_t = min(9, int(s1[i]) + 1)
            min_d = 10 ** (len(s1) + 1)
            best_n1 = []
            best_n2 = []

            for t in range(min_t, max_t + 1):
                n1, n2 = solve(s1[i:], str(t) + s2[i + 1:])
                d = abs(int("".join(n1)) - int("".join(n2)))
                if d < min_d:
                    min_d = d
                    best_n1 = n1
                    best_n2 = n2
            r1.extend(best_n1)
            r2.extend(best_n2)
            break


    return r1, r2

def playout(s,repl):
    r = []
    for c in s:
        if c == "?":
            r.append(repl)
        else:
            r.append(c)

    return r


for t in range(num_cases):
    s1,s2 = fin.readline().strip().split()

    r1,r2 = solve(s1, s2)

    print("Case #{}: {} {}".format(t + 1, "".join(r1), "".join(r2)))
