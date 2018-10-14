#! /usr/bin/python3


N = int(input())


for case in range(N):
    input()
    candies =list(map(int, input().split())) 
    answer = 0
    modifier = 0
    i = 0
    answer += sum(candies)
    bits = [ [] for i in range(32) ]
    test = {}
    for c in candies:
        test[c] = []
    for candy in candies:
        index = 0
        c = candy
        while c > 0:
            if c%2:
                bits[index].append(candy)
                test[candy].append(i)
            c //= 2
            index += 1

    def remove(value,bit):
        for i in test[value]:
            if len(bits[i]) == 0:
                pass

        

    possible = True
    for index in range(32):
        if len(bits[index]) % 2:
            possible = False
            break
        #if not remove(bits[-1],index):
        #    possible = False


    modifier = min(candies)
    if not possible:
        print("Case #%d: NO" % (case + 1))
    else: 
        print("Case #%d: %d" % (case +1,answer -modifier))

        
    

