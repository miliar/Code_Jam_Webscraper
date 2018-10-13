def findLargest(n):
    index = len(n) + 1
    for i in range(1, len(n)):
        if n[len(n) - i] < n[len(n) - i - 1]:
            index = len(n) - i - 1
            n[len(n) - i - 1] = str(int(n[len(n) - i - 1]) - 1)
    soln = ""
    for j in range(len(n)):
        # if j == index:
        #     soln += str(int(n[j]) - 1)
        if j > index:
            soln += '9'
        else:
            soln += n[j]
    return int(soln)

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    nL = []
    for j in str(n):
        nL.append(j)
    print("Case #{}: {}".format(i, findLargest(nL)))
