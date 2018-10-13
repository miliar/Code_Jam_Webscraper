import sys
import numpy as np

def make_ints(l):
    return [int(i) for i in l.split(' ')]

def get_only_dec_speed(horses):
    new_horses = [horses[0]]
    min_speed = horses[0][1]
    for horse in horses[1:]:
        speed = horse[1]
        if speed < min_speed:
            min_speed = speed
            new_horses.append(horse)
    return new_horses

def get_ttm(horse1, horse2):
    if horse1[1] == horse2[1]:
        print "wtf", horse1, horse2
    return float(horse1[0]-horse2[0])/(horse2[1]-horse1[1])

def reduce_horses(horses):
    time_to_meet = [get_ttm(horse1, horse2) for (horse1, horse2) in zip(horses[:-1],horses[1:])]
    min_horse = np.argmin(time_to_meet)
    t = time_to_meet[min_horse]
    horses = horses[:min_horse] + horses[min_horse+1:]
    return horses, t

def solve_case(D, horses):
    #print horses
    horses = sorted(horses)
    #print horses
    horses = get_only_dec_speed(horses)
    #print horses
    horses     += [[D, 0]]
    while len(horses) > 1:
        horses, t = reduce_horses(horses)
        #print horses, t
        #print len(horses)
    return D/t 
    #horses     += [[D, 0]]
    # cur_pos     = horses[0][0]
    # cur_speed   = horses[0][1]
    # cur_time    = 0
    # print horses
    # for pos, speed in horses[1:]:
    #     if speed==cur_speed:
    #         continue
    #     pos += cur_time*speed
    #     t = float(cur_pos-pos)/(speed-cur_speed)
    #     if speed > cur_speed:
    #         print "====", t, speed, pos, cur_speed, cur_pos 
    #     if t < 0:
    #         continue
    #     if t*speed + pos > D:
    #         continue
    #     cur_time += t
    #     cur_pos  += t*cur_speed
    #     cur_speed = speed
    # return D/cur_time
                

def main():
    infile = sys.argv[1]
    inp = file(infile,"rb").read()
    lines = inp.splitlines()
    T = int(lines[0])
    lines = lines[1:]
    for case_num in range(T):
        D,N = make_ints(lines[0])
        test_case_lines = lines[1:][:N]
        horses = [make_ints(line) for line in test_case_lines]
        lines = lines[1+N:]
        ans = solve_case(D, horses)
        print "Case #%d: %0.6f"%(case_num+1,ans)

if __name__ == "__main__":
    # import time
    # start_time = time.time()
    # solve_case(100000, [(i+1,10000-i) for i in range(1000-1, 1, -1)])
    # print "Will take:", (time.time()-start_time)*100/60.
    main()