import sys
# read file

cases = []
with open(sys.argv[1]) as f:
   NUM = int( f.readline() )
   for i in range(0,NUM):
       this_line = int(f.readline())
       cases.append( this_line )

count=0
for element in cases:
    count +=1
    # Construct
    raw = []
    number = int(element)
    while( number!=0):
        raw.append(number%10)
        number = number/10
    # Result
    result = [raw[0]]
    for i in range(1, len(raw)):
        if raw[i] > min(result):
            result = []
            for j in range(0, i):
                result.append(9)
            result.append(raw[i]-1)
        else:
            result.append( raw[i] )
    result.reverse()
    print 'Case #{}: {}'.format( count, int(''.join(map(str, result))) )
