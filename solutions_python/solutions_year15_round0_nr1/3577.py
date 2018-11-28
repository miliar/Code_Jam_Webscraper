T = input()
for _ in range(int(T)):
    ppl = input().split()
    ppl = ppl[1]
    sum = 0
    cnt = 0
    for i in range(len(ppl)):
        if sum < i and int(ppl[i]) > 0:
            cnt += i - sum
            sum += cnt
        sum += int(ppl[i])
        # print(i, sum)
        # print('sum', sum)
    print("Case #"+str(_+1)+":", cnt)
