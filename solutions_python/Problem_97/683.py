f = open("C-large.in", 'r')
allfile = f.read()
lines = allfile.split("\n")
output = []
for x in xrange(1,len(lines)-1):
    nums = lines[x].split(" ")
    low = int(nums[0])
    high = int(nums[1])+1
    output.append(0)
    for y in xrange(low, high-1):
        st = str(y)
        orig = int(st)
        successes = []
        for temp in xrange(len(st)-1):
            st = st[-1:] + st[:-1]
            if st[0] != "0":
                numform = int(st)
                if orig < numform and numform < high:
                    if numform not in successes:
                        successes.append(numform)
                        output[x-1] += 1
                    

f = open("problem3.out", 'w')
for x in xrange(len(output)):
    f.write("Case #" + str(x+1) + ": " + str(output[x]) + "\n")
