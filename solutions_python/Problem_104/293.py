from itertools import combinations as cnr

if __name__ == "__main__":    
    with open("input", "rU") as fi:
        
        fo = open("output", "w")
        tests = long(fi.readline())
        
        for test in xrange(tests):
            
            line = fi.readline()
            nums = line.split()[1:]
            nums = map(long, nums)
            f = 0
            n = 2
            while(f == 0):
                if(n < len(nums) / 2):
                    #print n
                    sums = {}
                    for i in cnr(nums, n):
                        k = sum(i)
                        if k in sums.keys():
                            if not set(i).intersection(set(sums[k])):
                                fo.write("Case #" + str(test + 1) + ":" + "\n")
                                fo.write(" ".join(map(str, sums[k])) + "\n")
                                fo.write(" ".join(map(str, i)) + "\n")
                                #print sum(i), sum(sums[k]), k
                                f = 1
                                break
                        else:
                            sums[sum(i)] = i
                            
                    n = n + 1
                else:
                    f = 1
                    fo.write("Case #" + str(test + 1) + ":" + "\n")
                    fo.write("Impossible" + "\n")
        fo.close()
