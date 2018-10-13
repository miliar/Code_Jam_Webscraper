import re, string, sys, os, math

output = ''
outFile = "small_result.out"

os.chdir(os.path.dirname(__file__))

def oper(strIn):
    cnt = 0
    newLine = strIn.split(" ")
    A, B = [int(x) for x in newLine]

    if (B < A):
        return 0

    start = int(math.ceil(math.sqrt(A)))
    end = int(math.sqrt(B))

    for n in xrange(start, end + 1):
        s = str(n)
        rs = s[::-1]

        if s != rs:
            continue

        m = n * n

        s = str(m)
        rs = s[::-1]

        if s == rs:
            cnt += 1

    return cnt

def result_fout():
    global output

    try:
        fd = open(outFile, 'w+')
    except:
        print 'Fail to open %s.' % outFile
        sys.exit(-1)

    fd.write(output)
    fd.close()
    return


base_file = sys.argv[1]
try:
    base_fd = open(base_file, 'r')
except:
    print 'Fail to open %s.' % base_file
    sys.exit(-1)

lineNum = 0
T = 0
for line in base_fd:
    if T == 0:
        T = int(line)
        #print ('T:%d' % T)
    else:
        inStr = re.sub(r'\r|\n|\)', '', line)
        output += 'Case #%d: ' % lineNum + '%s\n' % oper(inStr)

    lineNum+=1

result_fout()
