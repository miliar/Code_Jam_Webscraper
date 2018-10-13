test_cases = int(raw_input())
for i in range(0,test_cases):
    cookie = 0.0000000
    time = 0.0000000
    rate = 2.0000000
    values = map(float,(raw_input().split()))
    flag = 0.0000000
    while 1:
        if values[0] < values[2]:
            new_time = time + values[0]/rate
            new_rate = rate + values[1]

            first_time = new_time + values[2]/new_rate
            second_time = time + values[2]/rate

            if first_time < second_time:
                time = new_time
                rate = new_rate
                flag = first_time
                continue
            else:
                print "Case #" + str(i+1) + ": " + str(round(second_time,7))
                break
        else:
            print "Case #" + str(i+1) + ": " + str(round(values[2]/rate,7))
            break
