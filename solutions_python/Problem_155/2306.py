testC = int(input())

for tc in range(testC):
    shy = [int(i) for i in input().split(" ")[1]]
    clap = shy[0]
    needed = 0
    for i in range(1, len(shy)):
        if clap < i and shy[i] != 0:
            needed += i - clap
            clap += i - clap
            #print("Needed",needed)
        clap += shy[i]
        #print("Clap", clap)
    print("Case #"+str(tc+1)+":", needed)
