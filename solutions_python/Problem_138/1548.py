text = open("dwar.in","rb")
output = open("deceit_answer.txt", "wb")
n = int(text.readline().strip("\n"))
for i in range(n):
    text.readline()
    naomi = text.readline().strip("\n")
    naomi = [float(j) for j in naomi.split()]
    naomi = sorted(naomi)
    ken = text.readline().strip("\n")
    ken = [float(j) for j in ken.split()]
    ken = sorted(ken)
    ken_copy = list(ken)
    score_deceit = 0
    score_war = 0
    for brickn in naomi[::-1]:
        max_ken = max(ken)
        min_ken = min(ken)
        if(max_ken < brickn):
            ken.remove(min_ken)
            score_war +=1
        else:
            ken.remove(max_ken)
    for brickk in ken_copy[::-1]:
        for j in range(len(naomi)):
            if(naomi[j] > brickk):
                break
        if(j != len(naomi) - 1):
            naomi.pop(j)
            score_deceit+=1
        else:
            if(naomi[-1] < brickk):
                naomi.pop(0)
            else:
                naomi.pop()
                score_deceit+=1
        
    output.write("Case #" + str(i + 1) +
                 ": "+ str(score_deceit) + " " + str(score_war) + "\n")
output.close()
text.close()
