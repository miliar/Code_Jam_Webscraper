def digits(n):
    l = []
    while (n > 0):
        l.append(n%10)
        n = int(n/10)
    l.reverse()
    return l

def solve(n):
    l = digits(n);
    done = False;
    while not done:
        done = True
        for i in range(len(l)-1):
            if l[i+1] < l[i]:
                l[i] -= 1
                for j in range(i+1, len(l)):
                    l[j] = 9
                    done = False;
    while (l[0] == 0):
        l = l[1:]
    fout.write("".join([str(x) for x in l]) + "\n")

lines = open("c:\codejam\B-small-attempt1.in").readlines()
fout = open("c:\codejam\B-small-attempt1.out", "w");
T = int(lines[0])
for tc in range(1, T+1):
    n = int(lines[tc]);
    fout.write("Case #" + str(tc) + ": ");
    solve(n);
fout.close()
