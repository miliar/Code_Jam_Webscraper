import numpy as np

def total_earn(gs,n_runs,n_seats):
    total = front = 0
    n_riders = np.sum(gs)
    for i_run in xrange(n_runs):
        queue = gs[front:] + gs[:front]
        earn,shift = ride_earn(queue,n_seats,n_riders)
        front = (front + shift) % len(gs)
        total += earn        
        if front == 0:
            full_cycles,runs_left = n_runs // (i_run+1), n_runs % (i_run+1)
            return full_cycles*total +  total_earn(gs,runs_left,n_seats)
    return total
    
        
def searchsorted_ge(arr,v):
    "last index i where v >= arr(i)"
    i_le = np.searchsorted(arr,v)
    return i_le - 1 if arr[i_le] > v else i_le

def ride_earn(gs,n_seats,n_riders):
    cumsum = 0
    for i_group,size in enumerate(gs):
        cumsum += size
        if cumsum > n_seats:
            return cumsum-size,i_group
    return n_riders,0

with open("roller_coaster.in","r") as fin: lines = iter(fin.readlines())

T = int(lines.next())
with open("roller_coaster.out","w") as fout:
    for i in xrange(1,T+1):
        R,k,N = map(int,lines.next().split())
        gs = map(int,lines.next().split())
        fout.write("Case #%i: %i\n"%(i,total_earn(gs,R,k)))
    