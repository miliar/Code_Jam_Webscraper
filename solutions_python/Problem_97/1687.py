import sys


def getnums(num1,num2):
    rec_pairs = []
    numpairs = 0
    newnum = num1 + 1
    while newnum < num2:
        str_rep = str(newnum)
        
        for x in range(1,len(str_rep)):
            str_rot = str_rep[x:] + str_rep[:x]
            num_rot = int(str_rot)
            l = newnum if num_rot > newnum else num_rot
            g = num_rot if l is newnum else newnum
            
            
            if l >= num1 and g <= num2 and l < g and (l,g) not in rec_pairs:
                #print "(",l,g,")"
                numpairs += 1
                rec_pairs.append((l,g))
        
        #sorted_by_first  = sorted(rec_pairs, key=lambda x: x[0])
        #sorted_by_second = sorted(rec_pairs, key=lambda x: x[1])
        
        newnum += 1

    return numpairs
if __name__ == "__main__":
    if len(sys.argv) > 1:
        f_in = open(sys.argv[1])
        lines = f_in.readlines()[1:]
        f_out = open('output.out', 'w')
        
        count = 1
        
        for l in lines:
            nums = l.split()
            f_out.write("Case #" + str(count) + ": " + str(getnums(int(nums[0]),int(nums[1]))) + "\n")
            count += 1
    else:
        while 1:
            nums = raw_input("> ").split()
            print getnums(int(nums[0]),int(nums[1]))