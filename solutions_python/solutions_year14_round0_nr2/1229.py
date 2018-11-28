



def solve(C,F,X):
    elapsed = 0.0
    rate = 2.0
    while C/rate + X/(F+rate) < X/rate:
        elapsed += C/rate
        rate += F
    elapsed += X/rate
    return elapsed
    

with open('large.in') as f:
    content = f.readlines()
content = [[float(j) for j in i.rstrip('\n').split()] for i in content]
for i in range(int(content.pop(0)[0])):
    print ('Case #' + str(i + 1) + ': ' + str(solve(content[0][0], content[0][1], content.pop(0)[2])))
