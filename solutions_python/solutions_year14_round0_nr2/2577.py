import sys

T = int(sys.stdin.next())
message = "Case #{0}: {1}"

case = 1
while case <= T:
    C, F, X = [float(x) for x in sys.stdin.next().strip().split()]
    # X = cookies needed to win
    # C = minimum cookies to buy a farm
    # F = additional cookies per second
    rate = 2.0
    if X <= C:
        print message.format(case, X / rate)
        case += 1
        continue
        
    t = C / rate
    while (X - C) / rate > X / (rate + F):
            t += C / (rate + F)
            rate += F

    # have C cookies
    finish_dt = (X - C) / rate
    print message.format(case, t + finish_dt)
    case += 1
