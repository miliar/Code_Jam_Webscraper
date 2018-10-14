with open('B-large.in', 'r') as a:
    text = a.readlines()
    a.close()
b = open('B-large.out', 'w+')
cases = int(text[0])
for i in range(1, cases + 1):
    index = 0
    inputs = []
    for n in range(0,len(text[i])):
        if n == (len(text[i]) - 1):
            inputs.append(float(text[i][index:n]))
        elif text[i][n] == " ":
            inputs.append(float(text[i][index:n]))
            index = n + 1
    c = inputs[0] #Farm Cost
    f = inputs[1] #Farm CPS
    x = inputs[2] #Cookie Goal
    
    cps = 2
    totalSec = 0
    prevTotal = x
    while ((x/cps) + totalSec) < prevTotal:
        prevTotal = totalSec + x/cps
        totalSec += c/cps
        cps += f
    b.write("Case #{}: %.7f\n".format(i) % prevTotal)
b.close()