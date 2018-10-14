f= open("B-large.in","r")
t= int(f.readline())
input = []
for i in range(0,t):
    input.append(f.readline())

f.close()
f = open("output.out","w")

def dance():
    for i in range(0,t):
        a = input[i].split(" ")
        b= []
        for e in a:
            b.append(int(e))
        googlers = b[0]
        surprise = b[1]
        min_score = b[2]
        scores = b[3:]
        cases =0
        for s in scores:
            base = s/3
            if s % 3 == 0:
                if base >= min_score:
                    cases+=1
                else:
                    if surprise>0 and base >0 and base+1 >= min_score:
                        cases += 1
                        surprise -= 1
            if s% 3 ==1:
                if base >= min_score or base+1 >=min_score :
                    cases+=1
                else:
                    if surprise >0 and base+1 >=min_score:
                        cases +=1
                        surprise -= 1
            if s%3 ==2:
                if base+1 >= min_score or base >=min_score:
                    cases+=1
                else:
                    if surprise >0 and base +2 >= min_score:
                        cases+=1
                        surprise -= 1
        f.write("Case #%s: %s \n" % (i+1,cases))
    f.close()

dance()
