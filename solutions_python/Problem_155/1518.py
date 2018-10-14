cases = int(input())

for case in range(cases):
    maxS, people = input().split(" ")
    maxS = int(maxS)
    people = list(map(int, list(people)))

    standing = 0
    needed = 0
    
    for i in range(len(people)):
        if people[i] > 0 and standing < i:
            needed += i - standing
            standing += i - standing
        standing += people[i]

    print("Case #{}: {}".format(case+1, needed))
