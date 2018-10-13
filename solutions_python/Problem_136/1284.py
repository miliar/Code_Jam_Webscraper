t = int(input())

for ttt in range(t):
    print("Case #%d:" % (ttt+1), end=" ")
    buf = input().split(" ")
    c = float(buf[0])
    f = float(buf[1])
    x = float(buf[2])
    wyn = x/2.0
    czas = 0
    tempo = 2.0
    for i in range(1,2*(10**6)):
        czas += c/tempo
        tempo += f
        pozostale = x/tempo
        wyn = min(wyn, czas + pozostale)
    print(wyn)