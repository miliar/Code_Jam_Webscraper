import sys
def read():  sys.stdout.flush(); return sys.stdin.readline().strip()

tests = int(read())
for test in xrange(tests):
    file_num, cap = [int(x) for x in read().split(" ")]
    files = [int(x) for x in read().split(" ")]
    
    files.sort(reverse = True)
    count = 0
    while files:
        if len(files) == 1:
            files = []
            count += 1
        elif files[0] + min(files) <= cap:
            a = files[0]
            b = max(fil for fil in files[1:] if fil <= cap - a)
            files.pop(0)
            files.remove(b)
            count += 1
        else:
            files.pop(0)
            count += 1
            
    print "Case #%d: %d" % (test+1, count)
