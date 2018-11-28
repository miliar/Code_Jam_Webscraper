# -*- coding: utf-8 -*-
from copy import copy

fname = "B-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

for caseno in range(numcases):
    print("Case", caseno)
    L, t, N, C, *dists = gcj_read()
    rep_dist = sum(dists)
    
    N_rep_pos = N % len(dists)
    journey_reps = N // len(dists)
    
    final_segment = dists[:N_rep_pos]

    
    # How far we get before boost
    initial_dist = t * 0.5
    
    N_dist = journey_reps * rep_dist + sum(final_segment)
    
    if N_dist < initial_dist:
        j_time = N_dist * 2
        
    else:
        reps_by_t = initial_dist // rep_dist
        extra_by_t = initial_dist % rep_dist
        #print(extra_by_t)
        
        if reps_by_t == journey_reps:
            # We're nearly there already
            final_segment.reverse()
            while final_segment[-1] <= extra_by_t:
                extra_by_t -= final_segment.pop()
            final_segment[-1] -= extra_by_t
            
            # Boost!
            final_segment.sort()
            final_segment[-L:] = [d/2 for d in final_segment[-L:]]
            #print(final_segment)
            
            j_time = t + (sum(final_segment)*2)
        else:
            next_segment = copy(dists)
            next_segment.reverse()
            while next_segment[-1] <= extra_by_t:
                extra_by_t -= next_segment.pop()
            next_segment[-1] -= extra_by_t
            
            reps_to_go = journey_reps - reps_by_t - 1 # The 1 is next_segment
            
            # Now journey is: next_segment + (reps_to_go * dists) + final_segment
            #print(next_segment, reps_to_go, dists, final_segment)
            effective_dist = 0.0
            
            dists.sort()
            next_segment.sort()
            final_segment.sort()
            while L > 0 and (dists or next_segment or final_segment):
                n = next_segment[-1] if next_segment else 0
                f = final_segment[-1] if final_segment else 0
                r = dists[-1] if dists else 0
                if next_segment and n >= f and n >= r:
                    effective_dist += n/2
                    #print("n",n, effective_dist)
                    next_segment.pop()
                    L -= 1
                elif final_segment and f >= r:
                    effective_dist += f/2
                    #print("f", f, effective_dist)
                    final_segment.pop()
                    L -= 1
                elif dists:
                    # Boost as many reps as we can
                    dists.pop()
                    if reps_to_go >= L:
                        effective_dist += (L * r/2) + ((reps_to_go - L) * r)
                        break
                    else:
                        effective_dist += (reps_to_go * r/2)
                        L -= reps_to_go
            #print(effective_dist, next_segment, reps_to_go, dists, final_segment)
            
            effective_dist += sum(next_segment) + sum(final_segment) + (reps_to_go * sum(dists))
            j_time = t + (effective_dist * 2)
            
    outstr = str(int(j_time))
    
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
