
fin = open("C-small.in", "r");
fout = open("C-small.out", "w");

T = int(fin.readline());

for t in range(T):
    (R, k, N) = eval("(" + fin.readline().replace(" ", ",") + ")");

    print R, k, N
    g = eval("[" + fin.readline().replace(" ", ",") + "]");

    nextgroup = [0]*N;
    countfrom = [0]*N;
    for i in range(N):
        j = i;
        total = 0;
        while (total + g[j] <= k and (total == 0 or j != i)):
            total += g[j];
            j = (j + 1) % N;

        nextgroup[i] = j;
        countfrom[i] = total;

    cur = 0;
    answer = 0;
    for r in range(R):
        answer += countfrom[cur];
        cur = nextgroup[cur];

    fout.write("Case #" + str(t+1) + ": " + str(answer) + "\n")

fout.close();
