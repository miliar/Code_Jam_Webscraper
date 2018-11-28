IN_FILE = "C_large.in"

infile = open(IN_FILE)
out = open("C.out","w")

cases = int(infile.readline())

def split(x):
    if x%2 == 1:
        return [x/2]
    else:
        return [x/2, x/2-1]

for case in range(cases):
    print "\n"
    print "Case #%i" %(case+1)
    out.write("Case #%i: " %(case+1))
    
    N,K = map(int,infile.readline().split())
    freqs = {N:1}
    steps = 0
    next_num_steps = 1
    while steps + next_num_steps < K:
        steps += next_num_steps
        next_num_steps *= 2
        new_freq = {}
        
        for x in freqs.keys():
            nums = split(x)
            split_freq = 1 if len(nums) == 2 else 2
            
            for num in nums:
                if not new_freq.has_key(num):
                    new_freq[num] = 0
                new_freq[num] += freqs[x]*split_freq
        freqs = dict(new_freq)
        assert 1 <= len(freqs.keys()) <= 2
        
        #print steps
        #print freqs
        
    m = max(freqs.keys())
    if K <= steps+freqs[m]:
        last_size = m
    else:
        last_size = min(freqs.keys())
    print last_size
    last_split = split(last_size)
    
    print max(last_split),min(last_split)
    out.write("%i %i\n" %(max(last_split),min(last_split)))
 
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()
out.close()