cases = int(raw_input())
for t in range(1, cases+1):
    s = list(raw_input().split()[-1])
    s = [int(c) for c in s]
    stand = 0
    required = 0
    for i in range(len(s)):
        if i > stand and s[i] != 0:
            required += (i - stand)
            stand += (i - stand)
            # print(i, stand, required)
        stand += s[i]
    print("Case #" + str(t) + ": " + str(required))


