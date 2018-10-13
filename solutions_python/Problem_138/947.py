def war(naomi, ken):
    result = 0

    while len(naomi)>0:
        ken = [x for x in ken if x>naomi[0]]
        if len(ken)==0:
            return len(naomi)
        elif len(ken)==1:
            return len(naomi)-1
        else:
            naomi.remove(naomi[0])
            ken.remove(ken[0])

    return result

def d_war(naomi, ken):
    result = 0

    while len(naomi)>0:
        if len(naomi) == 1:
            return result + int(naomi[0]>ken[0])
        else:
            if ready(naomi, ken):
                return len(naomi)
            else:
                naomi.remove(naomi[0])
                ken.remove(ken[-1])


def ready(naomi, ken):
    for i, v in enumerate(naomi):
        if v<ken[i]:
            return False
    return True



response = ""
f = open("in.txt", "r")
data = f.readlines()
f.close()

cases = int(data[0].rstrip())
for i in xrange(cases):
    n = [float(x) for x in data[i*3+2].rstrip().split()]
    k = [float(x) for x in data[i*3+3].rstrip().split()]
    n.sort(); k.sort();
    n1 = n[:]
    k1 = k[:]

    print n
    print k

    ans_war = war(n, k)
    ans_d_war = d_war(n1, k1)

    response += "Case #"+str(i+1)+": "+str(ans_d_war)+" "+str(ans_war)+"\n"


print response
f = open("out.txt", "w")
f.write(response)
f.close()