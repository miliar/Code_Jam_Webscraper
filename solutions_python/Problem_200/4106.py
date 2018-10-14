TC = int(input())
for tc in range(TC):
    N = input()
    ans = ""
    valid = True

    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            valid = False

    if valid == True:
        print("Case #{}: {}".format(tc+1, N))
    else:        
        if len(N) == 1:
            print("Case #{}: {}".format(tc+1, N))
        else:
            for i in range(len(N)-1):
                if int(N[i]) > int(N[i+1]):
                    if N[i] == "1":
                        ans = "9" * (len(N)-1)
                    else:
                        ans = str(int(N[i])-1) + "9" * (len(N[i:])-1)
                        j = i
                        while N[j] == N[j-1] and j != 0:
                            ans += "9"
                            j -= 1
                        lendiff = len(N)-len(ans)
                        ans = N[:lendiff] + ans
                    break
            print("Case #{}: {}".format(tc+1, ans))
