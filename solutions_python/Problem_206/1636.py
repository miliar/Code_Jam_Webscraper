for tc in range(int(raw_input())):
    ans = 0.0
    tot_distance,horses = map(int,raw_input().split())
    distance,speed = map(int,raw_input().split())
    time = 1.0*(tot_distance - distance)/speed
    cur_distance = distance
    cur_speed = speed
    for iterator in range(horses-1):
        distance,speed = map(int,raw_input().split())
        if cur_speed >= speed:
            if time < 1.0*(tot_distance - distance)/speed:
                time = 1.0*(tot_distance - distance)/speed
        else:
            cur_time = 1.0*(tot_distance - cur_distance)/cur_speed
            if(cur_time < 1.0*(tot_distance - distance)/speed):
                if time < 1.0*(tot_distance - distance)/speed:
                    time = 1.0*(tot_distance - distance)/speed
            else:
                if time < abs((1.0*(cur_distance - distance)*cur_speed/(speed-cur_speed))/cur_speed):
                    time = abs(((cur_distance - distance)*cur_speed/(speed-cur_speed))/cur_speed)
        """print cur_distance,cur_distance + abs((1.0*(cur_distance - distance)*cur_speed/(speed-cur_speed)))
        if cur_distance + abs((1.0*(cur_distance - distance)*cur_speed/(speed-cur_speed))) <= tot_distance:
            if time < abs((1.0*(cur_distance - distance)*cur_speed/(speed-cur_speed))/cur_speed):
                time = abs(((cur_distance - distance)*cur_speed/(speed-cur_speed))/cur_speed)
        else:
            if time < 1.0*(tot_distance - distance)/speed:
                time = 1.0*(tot_distance - distance)/speed"""
        cur_distance = distance
        cur_speed = speed
    ans = 1.0*tot_distance/time
    print "Case #"+str(tc+1)+": %0.6f" %ans
