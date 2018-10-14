

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    highs = 0
    lows = 0
    evens = 0
    odds = 0
    count = 0


    if K == 1:
        if N % 2 == 0:
            minAns = N / 2 - 1
            maxAns = N / 2
        else:
            minAns = N / 2
            maxAns = N / 2
        print("Case #{}: {} {}".format(i, maxAns, minAns))

    elif K == 2:
        high_num = N / 2
        if high_num % 2 == 0:
            minAns = high_num / 2 - 1
            maxAns = high_num / 2
        else:
            minAns = high_num / 2
            maxAns = high_num / 2
        print("Case #{}: {} {}".format(i, maxAns, minAns))

    elif K == 3:
        low_num = N / 2 - 1
        if low_num % 2 == 0:
            minAns = low_num / 2 - 1
            maxAns = low_num / 2
        else:
            minAns = low_num / 2
            maxAns = low_num / 2
        print("Case #{}: {} {}".format(i, maxAns, minAns))

    else:
        if N % 2 == 0:
            highs = 1
            lows = 1
        else:
            highs = 2
            lows = 0
        count = 3
        high_num = N/2


        while count <= N:

            #print "count: ", count

            #if high_num is odd
            if high_num % 2 != 0:
                odds = highs
                evens = lows
                highs = evens + 2 * odds
                lows = evens
            else:
                evens = highs
                odds = lows

                highs = evens
                lows = evens + 2 * odds
            high_num /= 2
            #print "highs: ", highs
            #print "lows: ", lows

            count += highs
            #print "count w/high:", count
            #print "high_num:", high_num

            if count >= K:
                if high_num % 2 == 0:
                    minAns = high_num / 2 - 1
                    maxAns = high_num / 2
                else:
                    minAns = high_num / 2
                    maxAns = high_num / 2
                print("Case #{}: {} {}".format(i, maxAns, minAns))
                break

            count += lows
            #print "count w/low", count
            if count >= K:
                low_num = high_num - 1
                if low_num % 2 == 0:
                    minAns = low_num / 2 - 1
                    maxAns = low_num / 2
                else:
                    minAns = low_num / 2
                    maxAns = low_num / 2
                print("Case #{}: {} {}".format(i, maxAns, minAns))
                break
