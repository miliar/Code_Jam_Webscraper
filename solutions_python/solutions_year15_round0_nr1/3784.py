import sys

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
		lines[i] = lines[i].lower().replace('\n','').replace('\r','').split(' ')
    #print lines
    return lines

lines = read_in()
loc = 0
tests = int(lines[loc][0])
loc += 1
# print lines
for i in xrange(0,tests):
    # print "test",i+1
    max_shy = int(lines[loc][0])
    audience = lines[loc][1]
    loc +=1
    # print audience
    if (max_shy == 0):
        print "Case #%d: 0"% (i+1)
        continue
    else:
        add = 0
        total = 0
        for a in xrange(0,max_shy+1):
            curr = int(audience[a])
            # print "curr, total", curr, total
            if (curr > 0 and a > total):
                add += a - total
                total += add+curr
                # print "add,total",add,total
            else:
                total += curr


        print "Case #%d: %d" %( i+1,add)
