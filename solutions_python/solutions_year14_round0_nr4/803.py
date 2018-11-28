def get_values(f,n):
    s = f.readline().strip()
    l = s.split(" ")
    num_l = []
    for i in l:
        x = float(i)
        num_l.append(x)
    return num_l

def get_war_score(n,k,num):
    n.sort(reverse = True)
    k.sort(reverse = True)
    score = 0
    for i in range(num):
        if(n[0]>k[0]):
            n.remove(n[0])
            x = k.pop()
            score += 1
        else:
            val = get_optimum_number(n[0],k)
            k.remove(val)
            n.remove(n[0])
    return score
   

def get_deceit_war_score(n,k,num):
    n.sort(reverse = True)
    k.sort(reverse = True)
    score = 0
    for i in range(num):
        if(k[0]>n[0]):
            k.remove(k[0])
            x = n.pop()
        else:
            val = get_optimum_number(k.pop(),n)
            n.remove(val)
            score += 1
    return score



def get_optimum_number(val,l):
    l.sort(reverse = True)
    i = 0
    for elem in l:
        if elem > val:
            i += 1
            continue
        else:
          break
    return l[i-1]

f = open("D-large.in")
f1 = open("output.txt","w")
s = f.readline().strip()

test_case = int(s)
naomi_values = []
ken_values = []

for i in range(test_case):
    s = f.readline().strip()
    N = int(s)
    naomi_values = get_values(f,N)
    ken_values = get_values(f,N)
    naomi_copy = naomi_values[:]
    ken_copy = ken_values[:]
    score_war = get_war_score(naomi_values[:],ken_values[:],N)
    score_deceit = get_deceit_war_score(naomi_values,ken_values,N)
    f1.write("Case #"+str(i+1)+": "+str(score_deceit)+" "+str(score_war)+"\n")
    

f.close()
f1.close()
