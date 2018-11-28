def solve(D, N, K, S):
    maxTime = 0;
    for i in range(N):
        length = float(D-K[i]);
        speed = S[i];
        tempTime = length/speed;
        if tempTime > maxTime:
            maxTime = tempTime;
    maxSpeed = float(D) / maxTime;
    fout.write("%.7f\n" % maxSpeed);

lines = open("c:\codejam\A-large.in").readlines()
fout = open("c:\codejam\A-large.out", "w");
T = int(lines[0])
counter = 1;
for tc in range(1, T+1):
    D = int(lines[counter].split()[0]);
    N = int(lines[counter].split()[1]);
    counter += 1
    K = []
    S = []
    for i in range(N):
        k_i = int(lines[counter].split()[0]);
        s_i = int(lines[counter].split()[1]);
        K.append(k_i);
        S.append(s_i);
        counter += 1;
    fout.write("Case #" + str(tc) + ": ");
    solve(D, N, K, S);
fout.close()
