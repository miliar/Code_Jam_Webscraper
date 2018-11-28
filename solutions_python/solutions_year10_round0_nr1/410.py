f = file("in")
lines = [l for l in f]
lines = lines[1:]
case = 0
for l in lines:
        case +=1
        nums = [int(x) for x in l.split(" ")]
        val= (str(bin(nums[1]))[2:]).zfill(nums[0])
        val[(-nums[0])]
        good = True
        for x in range(1,nums[0]+1):
                if val[-x]=='0':
                        good = False
                        break

        if good == True:
                val = "ON"
        else:
                val = "OFF"
        print "Case #%d: %s" % (case, val)
