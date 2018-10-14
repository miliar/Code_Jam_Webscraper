test_cases, case = int(input()), 1

for test in range(test_cases):
    print("Case #",end="")
    print(case, end="")
    print(": ", end="")
    num = int(input())
    naomi = sorted(map(float, input().split()))
    ken = sorted(map(float, input().split()))
    i = j = war = 0
    while(i<num and j<num):
        if ken[j] < naomi[i]:
            j += 1
        else:
            war += 1
            i += 1
            j += 1
    i = j = d_war = 0
    while(i<num and j<num):
        if ken[j] < naomi[i]:
            j += 1
            i += 1
            d_war += 1
        else:
            i += 1
    print(d_war, end=" ")
    print(num-war)
    case += 1


