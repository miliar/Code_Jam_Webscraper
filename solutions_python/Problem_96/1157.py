
normal_map = {}
surprise_map = {}
for n in range(0,31):
    normal_map[n] = set()
    surprise_map[n] = set()
    for i1 in range(0,11):
        for i2 in range(0,11):
            for i3 in range(0,11):
                sm = i1 + i2 + i3
                if sm!=n:
                    continue
                arr = [i1,i2,i3]
                #print (arr)
                arr.sort()
                #print (arr)
                mn = arr[0]
                mx = arr[2]
                arr = (arr[0], arr[1], arr[2])
                if mn==mx or mn+1==mx:
                    normal_map[n].add(arr)
                elif mn+2==mx:
                    surprise_map[n].add(arr)

#print normal_map
#print ("----------")
#print surprise_map

def has_min_p(p, arr_of_arrays):
    #print ("P:%d" %p )
    for arr in arr_of_arrays:
        #print (arr)
        #for item in arr:
        #    if item>=p:
        #        return True
        if arr[2]>=p: # best score > p?
            return True
    return False
    
def can_be_normal(num, p):
    if normal_map.has_key(num):
        return has_min_p(p, normal_map[num])
    return False

def can_be_surprise(num, p):
    if surprise_map.has_key(num):
        return has_min_p(p, surprise_map[num])
    return False

infile = open("B-large.in")
outfile = open("B-large.out", "w")

#infile = open("B.input.txt")
#outfile = open("B.output.txt", "w")

n = int(infile.readline())

for casenum in range(0, n):

    print ("Case %d" % casenum)
    nums = [int(s) for s in infile.readline().strip().split(" ")]
    num_goog = nums[0]
    surprises = nums[1]
    p = nums[2]
    g = nums[3:]
    total = 0
    #print ("Goog: %d, Surp: %d, p: %d\n" % (num_goog, surprises, p))

    for gi in g:
        #print ("P: %d, Gi: %d" % (p,gi))
        if can_be_normal(gi, p):
            #print("normal")
            total+=1
        elif surprises>0 and can_be_surprise(gi, p):
            #print("surprise")
            total+=1
            surprises-=1
        else:
            #print("-none-")
            pass
    #print("\n")
    outfile.write("Case #%d: %d\n" % (casenum+1, total))

infile.close()
outfile.close()

print("ok")

