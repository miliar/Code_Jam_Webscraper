file = open("B-large.in","r")
out = open("out.txt","w")

numCase = int(file.readline())
line = []
for y in range(1,numCase+1):
    ans = 0.0
    temp = 0.0
    div = 2.0
    line = file.readline().split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    if x < c:
        print >> out, "Case #"+str(y)+": "+str(x/div)
    else:
        temp = x/div
        while (x/div) > ((c/div) + (x/(div + f))):
            temp = temp + ((c/div) + (x/(div + f))) - (x/div)
            div = div + f
        print >> out, "Case #"+str(y)+": "+str(temp)

out.close()
file.close()
