f = open('Google Deceitful War Large.in','r')
g = open('Google Deceitful War Large.out','w')
def deceitful_war(Naomi,Ken):
    Naomi.sort()
    Ken.sort()
    Ken.reverse()
    N = 0
    K = 0
    for i in range(len(Naomi)):
        if Naomi[i] > min(Ken):
            v = min(Ken)
            Ken.remove(v)
            N += 1
        else:
            v = max(Ken)
            if Naomi[i] > v:
                N += 1
            else:
                K += 1
            Ken.remove(v)
    return N

def normal_war(Naomi,Ken):
    Naomi.sort()
    Ken.sort()
    N = 0
    K = 0
    for i in range(len(Naomi)):
        block = Naomi[i]
        v = [x for x in Ken if x > block]
        if v:
            v = min(v)
            K += 1
        else:
            N += 1
            v = min(Ken)
        Ken.remove(v)
    return N
        
       

def make_grid(a1,a2):
    answer = []
    for i in a1:
        row = []
        for j in a2:
            if i > j:
                row.append('W')
            if i < j:
                row.append('L')
        answer.append(row)
    return answer

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

cases = int(f.readline())
answers = []
for i in range(cases):
    n = f.readline()
    Naomi = f.readline().rstrip().split(' ')
    Ken = f.readline().rstrip().split(' ')
    Naomi = [float(x) for x in Naomi]
    Ken = [float(x) for x in Ken]
    Ken2 = Ken[:]
    deceit = deceitful_war(Naomi,Ken)
    normal = normal_war(Naomi,Ken2)
    answers.append("%s %s" %(str(deceit),str(normal)))

Google_print(g,answers)
f.close()
g.close()
    

