
with open("A-large.in") as file:
    T = int(file.readline())
    for i in range(T):
        input = file.readline().strip().split(" ")
        smax = int(input[0])
        inp = [int(j) for j in input[1]]
        initialSum = sum(inp)
        sum1  = inp[0]
        result = 0
        for t in range (1,smax+1):
            if t <= sum1:
                sum1+=inp[t]
            else:
                diff = t-sum1
                sum1+= (diff + inp[t])
                result += diff

        print("Case #" + str(i+1) +": " + str(result))




