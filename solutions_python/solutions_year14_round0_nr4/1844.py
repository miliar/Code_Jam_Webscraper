casenum = int(input())
num = []
naomi = []
ken = []
naomiscore =[0]*casenum
kenlow=0
kenhigh=0
naomilow=0
naomihigh=0
for i in range(casenum):
    num.append(int(input()))
    naomi.append(list(map(float,input().split())))
    ken.append(list(map(float,input().split())))

for i in range(casenum):
    kenlow=0
    naomilow=0
    naomi[i].sort()
    ken[i].sort()
    naomihigh = num[i] - 1
    kenhigh=naomihigh;
    for j in range(0,num[i]):
        if naomi[i][naomihigh] > ken[i][kenhigh]:
            naomiscore[i] = naomiscore[i] + 1
            kenlow = kenlow + 1
            naomihigh = naomihigh - 1
        else:
            kenhigh = kenhigh - 1
            naomihigh = naomihigh -1
score1 = naomiscore
naomiscore =[0]*casenum
for i in range(casenum):
    kenlow=0
    naomilow=0
    naomihigh = num[i] - 1
    kenhigh=naomihigh;
    for j in range(num[i]):
        if naomi[i][naomilow] > ken[i][kenlow]:
            kenlow = kenlow + 1
            naomilow = naomilow +1
            naomiscore[i] = naomiscore[i] + 1
        else:
            kenhigh = kenhigh - 1
            naomilow = naomilow + 1
score2 = naomiscore
for i in range(casenum):
    print('Case #{}:'.format(i+1),score2[i],score1[i])



