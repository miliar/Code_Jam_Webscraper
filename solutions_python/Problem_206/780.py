def max_horse_speed(k,speed,d):
    if k >= d:
        return 100000000000000
    time = float(d-k) / speed
    return float(d)/time

def do_one():
    D,N = map(int,raw_input().split())
    speed = 100000000000000
    for _ in xrange(N):
        k,s = map(int,raw_input().split())
        speed = min(max_horse_speed(k,s,D),speed)
    return speed

T = int(raw_input())
for i in xrange(T):
    print("CASE #" + str(i+1) + ": " + str(do_one()))