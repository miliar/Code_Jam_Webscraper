import math

def solve(N,K,R,H):
    #print(N, K, R, H)
    maxVal = -1;
    for i0 in range(len(R)):
        r = R[i0];
        h = H[i0];
        R1 = []
        H1 = []
        Mult1 = []
        removedFirstCopy = False;
        for i in range(N):
            if R[i] <= r:
                if R[i] == r and not removedFirstCopy:
                    removedFirstCopy = True;
                    continue;
                R1.append(R[i]);
                H1.append(H[i]);
                Mult1.append(R[i] * H[i]);
        #print ("R=", r, ": ")
        if len(R1) < K-1:
            continue;
        l = sorted(zip(Mult1, H1,R1), reverse=True);
        #print(l);
        #print("Pi * ", r, " * ", r);
        temp = math.pi * r*r + 2* math.pi * r*h;
        for i in range(K-1):
            temp += 2* math.pi * l[i][1] * l[i][2];
            #print("2*Pi * ", l[i][1], " * ", l[i][2], "=", temp);
        maxVal = max(maxVal, temp);
    fout.write('{0:.9f}'.format(maxVal) + "\n");

lines = open("c:\codejam\A-small-attempt0.in").readlines()
fout = open("c:\codejam\A-small-attempt0.out", "w");
T = int(lines[0]);
counter = 1;
for tc in range(1, T+1):
    #print("Case: ", tc)
    N = int(lines[counter].split()[0]);
    K = int(lines[counter].split()[1]);
    counter += 1
    R = []
    H = []
    for i in range(N):
        r_i = int(lines[counter].split()[0]);
        h_i = int(lines[counter].split()[1]);
        R.append(r_i);
        H.append(h_i);
        counter += 1;
    fout.write("Case #" + str(tc) + ": ");
    solve(N,K,R,H);
fout.close()
