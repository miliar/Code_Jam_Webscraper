#!/usr/bin/python



def find_anwser(C, F, X, time, cookies_per_second, cookies):        
    if cookies - C >= 0:
        with_house = find_anwser(C, F, X, time, cookies_per_second + F, cookies - C)
        return min(with_house, time + (X - cookies)/cookies_per_second)
    elif cookies_per_second < 500:
        return find_anwser(C, F, X, time + (C - cookies)/cookies_per_second, cookies_per_second, C)
    else:
        return time + (X - cookies)/cookies_per_second
    

ncases = int(raw_input())

for ncase in xrange(ncases):
    data = map(float, raw_input().split(' '))
    C, F, X = tuple(data)
 
    if X <= C:
        print 'Case #' + str(ncase + 1) + ': ' + str(X/2.0)
    else:
        house_times = [C/2.0]
        cookies_per_second = [2.0]
        min_time = X/2.0

        for i in xrange(int(X)/int(C)):
            new_cookies_per_second = cookies_per_second[i] + F
            new_time = house_times[i] + X/new_cookies_per_second 
            house_times.append(house_times[i] + C/new_cookies_per_second)
            cookies_per_second.append(new_cookies_per_second)

            min_time = min(min_time, new_time)

        print 'Case #' + str(ncase + 1) + ': ' + str(min_time)
