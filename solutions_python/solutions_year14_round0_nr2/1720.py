input = open("jamcode.txt")

T = int(input.readline())

for i in range(T):
    line = input.readline()
    data = [float(x) for x in line.split()]
    C = data[0]
    F = data[1]
    X = data[2]
    oncontinue = True
    n = -1
    previous_sum = float("inf")
    while (oncontinue):
        n += 1
        somme = X/(2+n*F)
        for j in range(n):
            somme += C/(2+j*F)
        if (somme > previous_sum):
            oncontinue = False
            print("Case #"+str(i+1)+": "+str(previous_sum))
        previous_sum = somme
