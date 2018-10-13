#!/usr/bin/env python3

cases = int(input())
for i in range(1, cases + 1):
    C, F, X = map(float, input().split())

    rate = 2 # 2 cookies a second
    cookies = 0
    time_spent = 0

    while cookies != X:
        if cookies == C:
            # check if we'd finish before the returns kick in
            cookies_left = X - cookies
            if cookies_left / rate > (cookies_left + C) / (rate + F):
                # buy the farm
                cookies = 0
                rate += F
            else:
                time_spent += cookies_left / rate
                break

        # wait till next event point
        wait_cookies = min(C, X)
        time_spent += wait_cookies / rate
        cookies = wait_cookies

    print("Case #" + str(i) + ": " + str(time_spent))
