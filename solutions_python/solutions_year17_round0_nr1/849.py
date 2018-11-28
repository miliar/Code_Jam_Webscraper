#pancake line

t = int(input())
for i in range(1,t+1):
    stacknum = input().split()
    series = list(stacknum[0])
    K = int(stacknum[1])
    numbers = []
    for s in range(0,len(series)):
        numbers.append(1 if series[s] == "+" else 0)
    N = len(numbers)
    impossible = False
    if(2 * K > N):
        #check if impossible
        overlap = numbers[N-K:K]
        if not ((not 0 in overlap) or (not 1 in overlap)):
            impossible = True
    if impossible:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:     
        flips = 0
        impossible2 = False
        while(True):
            if not 0 in numbers:
                break
            index_to_flip_from = 0
            while numbers[index_to_flip_from] == 1:
                index_to_flip_from += 1
                if index_to_flip_from + K > N:
                    impossible2 = True
                    break
            if impossible2:
                break
            for n in range(index_to_flip_from, index_to_flip_from + K):
                numbers[n] = 1 - numbers[n]
            flips += 1
        if impossible2:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            output = flips
            print("Case #{}: {}".format(i,output))