import sys
with open(sys.argv[1]) as input:
    content=input.readlines()
content.pop(0)
results=[]
for i,line in enumerate(content):
    S_levels=line.split()[1]
    standing=0
    needed=0
    for s_level ,nr in enumerate(S_levels):
        nr=int(nr)
        if s_level > standing:
            needed+=s_level-standing
            standing+=s_level-standing
        standing+=nr
    results.append("Case #{}: {}".format(i+1,needed))
with open("output.txt",'w') as output:
    output.write('\n'.join(results))