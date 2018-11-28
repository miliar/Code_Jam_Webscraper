inputs = open('codejamA.txt', "r")
tokens = []
for line in inputs:
    for token in line.split(' '):
        tokens.append(token.strip())

t = int(tokens[0])
for j in range(0, t):
    r1=int(tokens[34*j+1])
    r2=int(tokens[34*j+18])
    l1=tokens[1+34*j+1+4*r1-4 : 1+34*j+1+4*r1]
    l2=tokens[1+34*j+18+4*r2-4 : 1+34*j+18+4*r2]
    l=list(set(l1)&set(l2))
    if(len(l)>1):
        print "Case #"+str(j+1)+": Bad magician!"
    elif(len(l)==1):
        print "Case #"+str(j+1)+": "+l[0]
    else:
        print "Case #"+str(j+1)+": Volunteer cheated!"
    
