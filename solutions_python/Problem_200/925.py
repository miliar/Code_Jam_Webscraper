def tidyNumber(N):
    numbers = list()
    for s in list(str(N)):
        numbers.append(int(s))
        
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                return False
    return True
            
def nextNumber(N):
    numbers = list(str(N))
    for i in range(len(numbers) - 1, -1, -1):
        firstMayor = -1
        j = 0
        while j < i:
            if int(numbers[j]) > int(numbers[i]):
                firstMayor = j
            j = j + 1
        if firstMayor != -1:
            numbers[firstMayor] = str(int(numbers[firstMayor]) - 1)
            for k in range(firstMayor + 1, len(numbers)):
                numbers[k] = "9"
    return int("".join(map(str, numbers)))
        
        
    

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    while not tidyNumber(N):
        N = nextNumber(N)
        
    print("Case #{}: {}".format(i,N))
