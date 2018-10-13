def f(C, F, X):
    # T = x1(num) + X/(2+num*F)
    minimum = X/2
    num = 1
    xx = C/2
    while True:
        minimum = min(minimum, xx+X/(2+(num)*F))
        xx += C/(2+(num)*F)
        if xx >= minimum:
            return minimum
        num += 1

def g():
    i = 1;
    for line in input().splitlines()[1:]:
        line = [float(x) for x in line.split()]
        print("Case #"+str(i)+":", f(line[0], line[1], line[2]))
        i+=1
