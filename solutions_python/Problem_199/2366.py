def flip(s,ind, k):
    for i in range(ind, ind+k):
        if s[i] == '-':
            s[i] = '+'
        else:
            s[i] = '-';

def solve(s,k):
    counter = 0
    for i in range(0, len(s)-k+1):
        if s[i] == '-':
            flip(s, i, k);
            counter += 1
    if '-' in s:
        fout.write("IMPOSSIBLE\n");
    else:
        fout.write(str(counter)+"\n")

lines = open("c:\codejam\A-large.in").readlines()
fout = open("c:\codejam\A-large.out", "w");
T = int(lines[0])
for tc in range(1, T+1):
    s = list(lines[tc].split()[0]);
    k = int(lines[tc].split()[1]);
    fout.write("Case #" + str(tc) + ": ");
    solve(s, k);
fout.close()
