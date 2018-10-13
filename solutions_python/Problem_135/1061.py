f_in = open('A-small-attempt0.in', 'r')
f_out = open('A.out', 'w')


T = int(f_in.readline())
for case_id in range(T):
    L1 = int(f_in.readline().strip())
    G1 = [[int(x) for x in f_in.readline().strip().split()] for i in range(4)]
    S1 = set(G1[L1-1])
    L2 = int(f_in.readline().strip())
    G2 = [[int(x) for x in f_in.readline().strip().split()] for i in range(4)]
    S2 = set(G2[L2-1])
    S1S2 =  S1.intersection(S2)
    if len(S1S2)==1:
        f_out.write("Case #"+str(case_id+1)+": "+str(S1S2.pop())+"\n")
    elif len(S1S2)>=2:
        f_out.write("Case #"+str(case_id+1)+": Bad Magician!\n")
    else:
        f_out.write("Case #"+str(case_id+1)+": Volunteer Cheated!\n")