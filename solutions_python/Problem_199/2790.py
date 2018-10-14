n = int(input())

for b in range(n):
    try:
        count = 0
        no,pansize = input().split(" ")
        pansize = int(pansize)
        no = list(no)
        for i in range(len(no)):
            if no[i]=="-":
                j = i
                # print(j)
                # print(pansize)


                for j in range(j+pansize):
                    if no[j] == "-":
                        no[j]='+'
                    elif no[j]=="+":
                        no[j]='-'
                    # print(no)
                count+=1

        print("Case #{}: {}".format(b + 1, count))
    except:
        print("Case #{}: IMPOSSIBLE".format(b + 1))