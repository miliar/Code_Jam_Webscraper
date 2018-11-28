from math import ceil

def war(j, arrayN, arrayK):
    tempN = arrayN[:]
    tempK = arrayK[:]
    for i in range(j):
        minN = tempN.pop(0)
        minK = list(filter(lambda x: x > minN, tempK))
        if len(minK) == 0:
            return len(tempK)
        else:
            tempK.pop(tempK.index(minK[0]))
    return 0

def dwar(j, arrayN, arrayK):
    score = 0
    tempN = arrayN[:]
    tempK = arrayK[:]
    for i in range(j):
        if tempN[0] > tempK[0]:
            score += 1
            tempN.pop(0)
            tempK.pop(0)
        else:
            tempN.pop(0)
            tempK.pop(-1)
    return score

def main():
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    N = int(f1.readline().rstrip())
    for i in range(N):
        j = int(f1.readline().rstrip())
        arrayN = map(float, f1.readline().rstrip().split())
        arrayK = map(float, f1.readline().rstrip().split())
        arrayN = sorted(arrayN)
        arrayK = sorted(arrayK)
        score = war(j, arrayN, arrayK)
        dscore = dwar(j, arrayN, arrayK)
        f2.write("Case #" + str(i+1) + ": " + str(dscore) + " " + str(score) + "\n")

main()
