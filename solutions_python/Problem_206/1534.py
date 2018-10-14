import sys

last_number = 0
sys.setrecursionlimit(2000)

input = open('gsR23v1.txt', 'r')
tests = int(input.readline())
# print (tests)

for i in range(1,tests+1):
    case = input.readline()
    (d,n) = case.split(' ')
    d = int(d)
    n = int(n)
    min_speed = 0
    for j in range(1,int(n)+1):
        horse = input.readline()
        (k,s) = horse.split(' ')
        k=int(k)
        s=int(s)
        # if d-k>0:
        current_speed = d/((d-k)/s)
        # else:
        #     current_speed = min_speed
        if min_speed is 0 or current_speed < min_speed:
            min_speed = current_speed

    # (mx,mi)=func(int(n),int(k))
    print ('Case #%s:'%i,'%.6f'%min_speed)
