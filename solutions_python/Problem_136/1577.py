import string

def goal_time(start_cookie, current_time, rate, goal):
    return current_time + (goal - start_cookie) / rate

f = open('B-large.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1

while count <= n:
    line = string.split(f.readline()[:-1], ' ')
    cost, clicker_rate, win = [float(x) for x in line]

    time = 0.0
    cookies = 0.0
    rate = 2.0
    t0 = goal_time(cookies, time, rate, cost) # time, buy cookie clicker
    t1 = goal_time(cookies, time, rate, win) # win time, w/o buying clicker
    t2 = goal_time(0.0, t0, rate + clicker_rate, win) # win time, buy clicker
    
    if(t1 < t2):
        g.write("Case #%d: %0.7f\n" % (count, t1))
        count += 1
        continue
    
    while(t2 < t1):
        time = t0
        cookies = 0.0
        rate += clicker_rate
        t0 = goal_time(cookies, time, rate, cost) 
        t1 = goal_time(cookies, time, rate, win) 
        t2 = goal_time(0.0, t0, rate + clicker_rate, win)
    g.write("Case #%d: %0.7f\n" % (count, t1))

    count += 1

f.close()
g.close()