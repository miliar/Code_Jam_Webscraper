import sys

def magictrick(a, arr1, b, arr2):
    #print "%i, %s, %i, %s"%(a, str(arr1), b, str(arr2))
    s1 = set(arr1[a-1])
    s2 = set(arr2[b-1])
    intersect = s1.intersection(s2)
    #print "intersect: %s"%(str(intersect))
    if len(intersect)==1:
        return str(intersect.pop())
    elif len(intersect)==0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"
    
def procfile(fname):
    retval = []
    with open(fname, "r") as f:
        n = int(f.readline())
        for i in range(n):
            a = int(f.readline())
            arr1 = [[]]*4
            for j in range(4):
                arr1[j] = [int(s) for s in f.readline().split()]
            b = int(f.readline())
            arr2 = [[]]*4
            for j in range(4):
                arr2[j] = [int(s) for s in f.readline().split()]
            retval.append((a, arr1, b, arr2))
    return retval
        
def main():
    fname = sys.argv[1]
    result = procfile(fname)
    cnt = 1
    #print "["
    for (a, arr1, b, arr2) in result:
        print "Case #%d: %s"%( cnt, magictrick(a, arr1, b, arr2))
        cnt = cnt+1
    #print "]"
    
if __name__ == "__main__":
    main()