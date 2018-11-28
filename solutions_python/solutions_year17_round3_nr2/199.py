import sys

def included(inter,e,s):
    return inter[0]>=e and inter[1]<=s


def greedy(c_act,j_act,sc,sj):
    c_act = sorted(c_act,key=lambda x:x[0])
    j_act = sorted(j_act,key=lambda x:x[0])
    mc = len(c_act)
    mj = len(j_act)
    c_gap = []
    for i in range(mc):
        e = c_act[i][1]
        s = c_act[(i+1)%mc][0]
        if s<e:
            s+=2*720
        notinc = True
        for inter in j_act:
            if included(inter,e,s):
                notinc=False
                break
        if notinc:
            d = s-e
            c_gap.append((d,i))
    j_gap = []
    for i in range(mj):
        e = j_act[i][1]
        s = j_act[(i+1)%mj][0]
        if s<e:
            s+=2*720
        notinc = True
        for inter in c_act:
            if included(inter,e,s):
                notinc=False
                break
        if notinc:
            d = s-e
            j_gap.append((d,i))
    c_gap = sorted(c_gap,key=lambda x: x[0])
    j_gap = sorted(j_gap,key=lambda x: x[0])
    pc,pj = 0,0
    while (pc<len(c_gap)-1) or (pj<len(j_gap)-1):
        if (mc-pc)>(mj-pj):
            if (sc+c_gap[pc][0])>720:
                break
            else:
                sc+=c_gap[pc][0]
                pc+=1
        elif (mc-pc)<(mj-pj):
            if (sj+j_gap[pj][0])>720:
                break
            else:
                sj+=j_gap[pj][0]
                pj+=1
        elif (sj+j_gap[pj][0])<(sc+c_gap[pc][0]):
            if (sj+j_gap[pj][0])>720:
                break
            else:
                sj+=j_gap[pj][0]
                pj+=1
        else:
            if (sc+c_gap[pc][0])>720:
                break
            else:
                sc+=c_gap[pc][0]
                pc+=1
    return 2*max(mc-pc,mj-pj)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = [int(x) for x in input().split()]
    Ac,Aj = line[0],line[1]
    c_act = []
    sc = 0
    for j in range(Ac):
        c_act.append([int(x) for x in input().split()])
        if c_act[-1][1]<c_act[-1][0]:
            c_act[-1][1]+=2*720
        sc+=c_act[-1][1]-c_act[-1][0]
    j_act = []
    sj = 0
    for j in range(Aj):
        j_act.append([int(x) for x in input().split()])
        if j_act[-1][1]<j_act[-1][0]:
            j_act[-1][1]+=2*720
        sj+=j_act[-1][1]-j_act[-1][0]
    res = greedy(c_act,j_act,sc,sj)

    print("Case #{}: {}".format(i, res))
        # print(i, file=sys.stderr) #DEBUG
