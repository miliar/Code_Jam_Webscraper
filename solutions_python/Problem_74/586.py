def get_steps(seq):
    prev_target=seq[0]
    handicap=steps=0    
    position={"O":1,"B":1}
    for s in seq:
        if s.isnumeric():
            step=abs(position[target]-int(s))+1
            position[target]=int(s)
            if prev_target!=target:
                steps+=handicap                
                handicap=max(1,step-handicap)                                
            else:
                handicap+=step
            prev_target=target    
        else:
            target=s
    return steps+handicap

fin=open("in.txt")
fout=open("out.txt",mode="w")
i=0
for line in fin:
    s=line.rstrip().split()
    s.pop(0)
    if s: print("Case #{}:".format(i),get_steps(s),file=fout)
    i+=1