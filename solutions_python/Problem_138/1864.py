import random

Filename = 'D-small-attempt1.in'

with open(Filename,'r') as file_seq:
    all_lines = list()
    for line in file_seq.readlines():
        line = line.rstrip().split()
        x = list()
        for i in range(len(line)):
            x.append(float(line[i]))
        all_lines.append(x)

numCases = int(all_lines[0][0])

r = len(all_lines[1:])
i = 1
k = 1
cases = dict()

while i < r:
    first = all_lines[i][0]
    case = list()
    i = i + 1
    for j in range(2):
        case.append(all_lines[i])
        i = i + 1
    cases[k] = first,case
    k = k + 1


def balance(ch_ken, ch_naomi):
    if ch_ken > ch_naomi:
        return 1
    if ch_ken < ch_naomi:
        return -1
    if ch_ken == ch_naomi:
        return 0    

def playWar(ken1, naomi1,n):
    pts_ken = 0
    pts_naomi = 0
    for i in range(n):
        ch_naomi = naomi1.pop(random.randint(0,len(naomi1)-1))
        diff_list = [ch_naomi - ken1[j] for j in range(len(ken1))]
        diff_list2 = [abs(diff_list[j]) for j in range(len(diff_list))
                     if diff_list[j]<0]
        if len(diff_list2) != 0:
            x = min(diff_list2)
            ch_ken = ch_naomi + x
            ch_ken = ken1.pop(ken1.index(round(ch_ken,4)))   
        else:
            ch_ken = ken1.pop(ken1.index(min(ken1)))
        t = balance(ch_ken,ch_naomi)
        if t == 1:
            pts_ken = pts_ken + 1
        if t == -1:
            pts_naomi = pts_naomi + 1
        if t == 0:
            continue
    return pts_ken,pts_naomi


def playDecietfulWar(ken,naomi,n):
    pts_ken = 0
    pts_naomi = 0
    for i in range(n):
        if len(naomi) > 1:
            ch_naomi1 = min(naomi)
        sort_ken = sorted(ken,reverse = True)
        if len(sort_ken) >1:
            x,y = sort_ken[0],sort_ken[1]
            r = random.uniform(y,x)
            while r in sort_ken:
                r = random.uniform(y,x)
        else:
            r = sort_ken[0] - 0.01
        told_naomi = r
        diff_list = [told_naomi - ken[j] for j in range(len(ken))]
        diff_list2 = [abs(diff_list[j]) for j in range(len(diff_list))
                     if diff_list[j]<0]
        if len(diff_list2) != 0:
            x = min(diff_list2)
            ch_ken = told_naomi + x
            ch_ken = ken.pop(ken.index(ch_ken))
        else:
            ch_ken = ken.pop(ken.index(min(ken)))
        ch_naomi = [naomi[j] for j in range(len(naomi))
                    if naomi[j] > ch_ken]
        if len(ch_naomi) ==0:
            ch_naomi = naomi.pop(naomi.index(min(naomi)))
        else:
            ch_naomi = min(ch_naomi)
            naomi.pop(naomi.index(ch_naomi))
        t = balance(ch_ken,ch_naomi)
        if t == 1:
            pts_ken = pts_ken + 1
        if t == -1:
            pts_naomi = pts_naomi + 1
        if t == 0:
            continue
    return pts_ken,pts_naomi    

naomi_pts = list()
ken_pts = list()
naomi_pts_deciet = list()

for i in range(int(numCases)):
    n,naomi,ken = cases[i+1][0],cases[i+1][1][0],cases[i+1][1][1]
    pts_ken,pts_naomi1 = playWar(ken,naomi,int(n))
    ken_pts.append(pts_ken)
    naomi_pts.append(pts_naomi1)


with open(Filename,'r') as file_seq:
    all_lines = list()
    for line in file_seq.readlines():
        line = line.rstrip().split()
        x = list()
        for i in range(len(line)):
            x.append(float(line[i]))
        all_lines.append(x)

numCases = int(all_lines[0][0])

r = len(all_lines[1:])
i = 1
k = 1
cases = dict()

while i < r:
    first = all_lines[i][0]
    case = list()
    i = i + 1
    for j in range(2):
        case.append(all_lines[i])
        i = i + 1
    cases[k] = first,case
    k = k + 1
    
for i in range(int(numCases)):
    n,naomi,ken = cases[i+1][0],cases[i+1][1][0],cases[i+1][1][1]
    pts_ken,pts_naomi2 = playDecietfulWar(ken,naomi,int(n))

    ken_pts.append(pts_ken)
    naomi_pts_deciet.append(pts_naomi2)


filename2 = 'D-small-attempt1-output.txt'

with open(filename2, 'w') as file_seq:
    for i in range(0,int(numCases)):
        s = 'Case #'+str(i+1)+': '+str(naomi_pts_deciet[i])+' '+str(naomi_pts[i])+'\n'
        file_seq.writelines(s)
