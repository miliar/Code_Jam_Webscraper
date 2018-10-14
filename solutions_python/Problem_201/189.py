with open('C-large.in','r') as f, open('out.txt','w') as fout:
    t=int(f.readline().strip())
    lines=[s.strip() for s in f.readlines()]
    for case,line in enumerate(lines):
        n,k=[int(s) for s in line.split()]
        intervals={n:1}
        while k>intervals[max(intervals.keys())]:
            max_interval=max(intervals.keys())
            n_max=intervals[max_interval]
            k-=n_max
            intervals.pop(max_interval)
            intervals[max_interval//2]=intervals.get(max_interval//2,0)+n_max
            intervals[(max_interval-1)//2]=intervals.get((max_interval-1)//2,0)+n_max
        smax=max(intervals.keys())//2
        smin=(max(intervals.keys())-1)//2
        print('Case #%d:'%(case+1),smax,smin,file=fout)
