in_file = "B-large.in"
out_file = "B-large.out"


def getNum(time):
    parts = time.split(':')
    return int(parts[0])*100 + int(parts[1])

def addToTime(time, minute):
    hr = int(time/100)
    mm = time%100
    x = mm + minute
    if x >= 60:
        x = x%60
        hr = hr+1      
    return hr*100 + x

def solve(departs_from_A, arrives_to_B, departs_from_B, arrives_to_A):
    fromA = fromB = 0
    while departs_from_A:
        deprt_A = departs_from_A[0]
        if arrives_to_A and deprt_A >= arrives_to_A[0]:
            arrives_to_A.pop(0)
        else:
            fromA += 1
        departs_from_A.pop(0)

    while departs_from_B:
        deprt_B = departs_from_B[0]
        if arrives_to_B and deprt_B >= arrives_to_B[0]:
            arrives_to_B.pop(0)
        else:
            fromB += 1
        departs_from_B.pop(0)

    return str(fromA) + " " + str(fromB)            

fr = open(in_file, 'r')
fw = open(out_file, 'w')
num_cases = int(fr.readline().strip())
for i in xrange(num_cases):
    t_time = int((fr.readline()))
    ns = fr.readline().split(' ')
    na = int(ns[0])
    nb = int(ns[1])
    departs_from_A = []
    arrives_to_B = []
    for j in xrange(na):
        times = fr.readline().split(' ')
        departs_from_A.append(getNum(times[0]))
        arrives_to_B.append(addToTime(getNum(times[1]), t_time))

    departs_from_B = []
    arrives_to_A = []   
    for j in xrange(nb):
        times = fr.readline().split(' ')
        departs_from_B.append(getNum(times[0]))
        arrives_to_A.append(addToTime(getNum(times[1]), t_time))
    
    departs_from_A.sort()
    arrives_to_B.sort()
    departs_from_B.sort()    
    arrives_to_A.sort()
    
    s = solve(departs_from_A, arrives_to_B, departs_from_B, arrives_to_A)                        
    #print s
    fw.write("Case #" + str(i+1) + ": " + s + "\n")

fr.close()
fw.close()
