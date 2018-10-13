import glob

def candysplit(ray):
    axor=0
    for x in ray:
        axor=axor^x
    if axor!=0:
        return "NO"
    ray.sort()
    return str(sum(ray[1:]))

for fname in glob.glob("C-*.in"):
    fp=open(fname)
    result=[]
    for i in range(int(fp.readline())):
        fp.readline()
        input=[int(x) for x in fp.readline().split()]
        result.append("Case #%i: %s"%(i+1,candysplit(input)))
    fp.close()
    fp=open(fname.split(".")[0]+".out","w+")
    fp.write("\n".join(result))
    fp.close()