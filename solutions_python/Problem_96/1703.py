#Google Dancers

d = {}
scores = {}
for i in range(31):
    d[i] = {'normal':[],'surprising':[]}
for i in range(11):
    normal = [(i,i,i)]
    surprising = []
    if i+1 <= 10:
        normal.append((i,i,i+1))
        normal.append((i,i+1,i+1))
    if i+2 <= 10:
        surprising.append((i,i,i+2))
        surprising.append((i,i+1,i+2))
        surprising.append((i,i+2,i+2))
    for j in normal:
        d[sum(j)]['normal'].append(j)
    for j in surprising:
        d[sum(j)]['surprising'].append(j)

#scores = what values score can be surprising

for i in range(11):
    scores[i] = []

for i in range(31):
    for j in d[i]['surprising']:
        temp = set(j)
        for k in temp:
            scores[k].append(sum(j))


never_surprising = [i for i in d.keys() if not d[i]['surprising']]
can_be_surprising = [i for i in range(31) if i not in never_surprising]

def most_bests(score,surps,array):
    answer = 0
    array.sort()
    for i in scores[score]:
        if i in array and surps > 0:
            array.remove(i)
            surps -= 1
            answer += 1
    for i in array:
        for j in d[i]['normal']:
            if max(j) >= score:
                answer += 1
                break
    return answer

f = open('Google Dancers.in','r')
g = open('Google Dancers.out','w')

cases = int(f.readline())
for i in range(cases):
    line = f.readline().rstrip()
    line = line.split(' ')
    line = [int(n) for n in line]
    surps = line[1]
    score = line[2]
    array = line[3:]
    g.write("Case #%s: %s\n" %(str(i+1),str(most_bests(score,surps,array))))
print "Done."
f.close()
g.close()


        
    




        
