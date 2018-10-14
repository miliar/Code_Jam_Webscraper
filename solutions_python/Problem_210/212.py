from collections import deque

def computeGaps(l):
    gapsC = []
    gapsJ = []
    mustTurn = 0;
    for i in range(len(l)-1):
        if l[i+1][2] != l[i][2]:
            mustTurn += 1;
        gap = l[i+1][0]-l[i][1];
        if (l[i+1][2] == "AC" and l[i][2] == "AC"):
            gapsC.append(gap);
        elif (l[i+1][2] == "AJ" and l[i][2] == "AJ"):
            gapsJ.append(gap);
    if l[-1][2] != l[0][2]:
        mustTurn += 1;
    gap = 24*60-l[-1][1] +l[0][0];
    if (l[-1][2] == "AC" and l[0][2] == "AC"):
        gapsC.append(gap);
    elif (l[-1][2] == "AJ" and l[0][2] == "AJ"):
        gapsJ.append(gap);
    return deque(sorted(gapsC)), deque(sorted(gapsJ)), mustTurn

def solve(AC, AJ, C,D,J,K):
    Ctag = ["AC"]*len(C);
    lC = sorted(zip(C, D, Ctag));
    Jtag = ["AJ"]* len(J);
    lJ = sorted(zip(J, K, Jtag));
    l = sorted(lC + lJ);
    gapsC, gapsJ, mustTurn = computeGaps(l);
    totalAC = sum([D[i]-C[i] for i in range(len(C))]);
    totalAJ = sum([K[i]-J[i] for i in range(len(J))]);
    while (totalAC <= 720 and len(gapsC)>0):
        totalAC += gapsC[0];
        gapsC.popleft();
    while (totalAJ <= 720 and len(gapsJ)>0):
        totalAJ += gapsJ[0];
        gapsJ.popleft();
    numOfTurns = mustTurn + 2*len(gapsC) + 2*len(gapsJ);
    if totalAC > 720:
        numOfTurns += 2;
    if totalAJ > 720:
        numOfTurns += 2;
    fout.write(str(numOfTurns) + "\n");

lines = open("c:\codejam\B-large.in").readlines()
fout = open("c:\codejam\B-large.out", "w");
T = int(lines[0]);
counter = 1;
for tc in range(1, T+1):
    print("Case: ", tc)
    AC = int(lines[counter].split()[0]);
    AJ = int(lines[counter].split()[1]);
    counter += 1
    C = []
    D = []
    J = []
    K = []
    for i in range(AC):
        J.append(int(lines[counter].split()[0]));
        K.append(int(lines[counter].split()[1]));
        counter += 1;
    for i in range(AJ):
        C.append(int(lines[counter].split()[0]));
        D.append(int(lines[counter].split()[1]));
        counter += 1;
    fout.write("Case #" + str(tc) + ": ");
    solve(AC, AJ, C,D,J,K);
fout.close()
