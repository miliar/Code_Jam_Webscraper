def get_candies(nums):    
    xor=0
    for n in nums: xor^=n
    if xor: return "NO"
    return "NO" if xor else sum(nums)-min(nums)    
    

fin=open("in.txt")
fout=open("out.txt",mode="w")
i=1
for line in fin:
    s=[int(s) for s in line.rstrip().split()]
    if len(s)<2: continue
    print("Case #{}:".format(i),get_candies(s),file=fout)
    i+=1