import math

def simplify(N, K):
    power = 2**int(math.log(K,2))
    mean = (N+1)/power - 1
    frac = ((K+1)-power)/power
    if frac <= mean - int(mean):
        return math.ceil(mean)
    else:
        return int(mean)

TestCases = int(input(""))
number = 0
for i in range(TestCases):
    number+=1
    line = input("")
    Parts = line.split(" ")
    N = int(Parts[0])
    K = int(Parts[1])
    result = simplify(N, K) - 1
    remainder = result % 2
    real = [int(result/2) + remainder , int(result/2)]
    print("CASE #" + str(number) + ": " + str(real[0]) + " " + str(real[1]))

