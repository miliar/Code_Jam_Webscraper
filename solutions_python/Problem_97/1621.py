# forgive me for this mess of code, since i'm tired after a long distance hiking

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    diglen = len(str(A))
    exp10 = 10 ** (diglen - 1)
    res = []
    for i in range(A, B):
        ror_i = i
        for j in range(1, diglen):
            tmp = ror_i % 10
            ror_i = ror_i // 10 + tmp * exp10
            if tmp > 0 and ror_i > i and ror_i <= B:
                if not (i, ror_i) in res:
                    res = res + [(i, ror_i)]
    print("Case #%d: %d" %(t + 1, len(res)))

