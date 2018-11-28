import numpy as np

f = open("A.in")
num = int(f.readline())
output = ""
for n in range(num):
    N, max_size = [int(x) for x in f.readline().strip().split(" ")]
    files = [int(x) for x in f.readline().strip().split(" ")]
    files.sort()
    end = len(files)
    stopped = 0
    #print max_size, N, files
    last_file = len(files)
    saved = 0
    done = False
    for k in range(len(files)/2):
        found_match = False
        if done == True:
            break
        for last in range(0, last_file)[::-1]:
            comb_size = files[k] + files[last]
            #print files[k], files[last], "=", comb_size,
            if k >= last:
                done = True
                break
            if comb_size <= max_size:
                #print "good"
                saved+=1
                found_match = True
                last_file = last
                break
            #print "bad"
    output_val = len(files) - saved
    print output_val
    output += "Case #"+str(n+1) + ": " + str(output_val) +"\n"

f = open ("A.out", "w+")
f.write(output)
f.close()


