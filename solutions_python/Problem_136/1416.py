def main():
    t = int(raw_input())
    case = 0
    while t > 0:
        t -= 1
        c, f, x = map(float, raw_input().split())
        cur_rate = 2.0
        ans = ( x * 1.0 ) / cur_rate
        best = ans
        time_spent = 0
        farm_count = 0
        k = 0
        #print "time spent on farm %s %s" % (0, ans)
        prev = 1<<31
        case += 1
        while True:
            k += 1
            farm_count += 1
            time_spent += (c * 1.0) / cur_rate
            cur_rate += f
            temp = time_spent + (x * 1.0 ) / cur_rate
            #print "time spent on farm %s %s" % (farm_count, temp)
            if temp > prev:
                break
            else:
                prev = temp
                best = min(best, temp)
        print "Case #%s: %s" % (case, best)

main()
