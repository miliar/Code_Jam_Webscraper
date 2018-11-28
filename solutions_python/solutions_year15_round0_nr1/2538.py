TC = int(input())
for t in range(TC):
    Smax, S = [i for i in input().split(" ")]
    Smax = int(Smax)
    S = [int(i) for i in S]
    stand, friend = 0, 0
    for index in range(len(S)):
        if S[index] != 0:
            if stand >= index:
                stand += S[index]
            else:
                friend += index - stand
                stand = index + S[index]
    print("Case #" + str(t+1) + ": " + str(friend))
