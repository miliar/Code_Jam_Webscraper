inputfile = open('B-small-attempt0.in', 'r')
T = int(inputfile.readline())
output = open("outputtidy.txt", 'w')
for i in xrange(1,T+1):
    number = int(inputfile.readline())
    it = number
    while it <= number:
        b = list(str(it))
        if sorted(b) == b:
            break
        else:
            it-=1
    output.write('Case #%d: %s\n' % (i, str(it)))
