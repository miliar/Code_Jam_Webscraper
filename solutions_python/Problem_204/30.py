import math

IN_FILE = "B_large.in"

infile = open(IN_FILE)
out = open("B.out","w")

def output(string):
    string = str(string)
    print string.rstrip("\n")
    out.write(string)

cases = int(infile.readline())

for case in range(cases):
    print "\n"
    output("Case #%i: " %(case+1))
    
    ning,npack = map(int,infile.readline().split())
    recipe = map(int,infile.readline().split())
    all_ranges = []
    
    Min = 9999999999
    Max = 0
    for i in range(ning):
        ing_ranges = []
        packs = map(int,infile.readline().split())
        for p in packs:
            low = int(math.ceil(p/1.1/recipe[i]))
            high = int(math.floor(p/0.9/recipe[i]))
            if low <= high:
                ing_ranges.append([low,high])
                Min = min(Min,low)
                Max = max(Max,high)
        ing_ranges.sort()
        all_ranges.append(ing_ranges)
    
    ans = 0
    serving = Max
    while serving >= Min:
        #print ""
        #print serving
        #print all_ranges
        success = True
        
        for i in xrange(ning):
            cur_range = all_ranges[i]
            if len(cur_range) == 0: 
                success = False
                break
            while len(cur_range) > 0 and cur_range[-1][0] > serving:
                del cur_range[-1]
            if len(cur_range) == 0: 
                success = False
                break
            #if cur_range[-1][0] <= serving <= cur_range[-1][1]:
            if cur_range[-1][1] < serving:
                success = False
                break
            
        #print success
        if success:
            for i in xrange(ning):
                del all_ranges[i][-1]
            ans += 1
        else:
            serving -= 1
            
    output(str(ans)+"\n")
 
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()
out.close()