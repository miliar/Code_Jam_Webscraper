#!/usr/bin/python3

for case in range(int(input())):
    C, F, X = map(float, input().split())
    t = 0
    rate = 2
    win = X / rate
    while True:
        wait = C / rate
        next_win = X / (rate + F)
        if win - wait > next_win:
            # continue
            t += wait
            rate += F
            win = next_win
        else:
            t += win
            break
    string = "{:.7f}".format(t)
    print("Case #{}: {}".format(case+1,string))