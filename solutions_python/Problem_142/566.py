from operator import itemgetter, attrgetter

def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = "Fegla Won" if res == None else str(res)
    outputLine = casestr+status
    print outputLine

def packstr(input_str):
    packed = []
    prev_c = None
    prev_count = 0
    for c in input_str:
        if c != prev_c:
            if prev_count > 0:
                packed.append( (prev_c, prev_count) )
            prev_c = c
            prev_count = 1
        else: prev_count += 1

    if prev_count > 0:
        packed.append( (prev_c, prev_count) )

    #print input_str, packed

    return packed

def main():
    T = int( raw_input() )

    for t in xrange(T):
        N = int( raw_input() )
        packed_str = packstr( raw_input() )
        str_def = map( lambda x:x[0], packed_str )
        chars = map( lambda x:[x[1]], packed_str )
        total_count = 0

        for n in xrange(1, N):
            packed_str = packstr( raw_input() )
            #print t, n, packed_str
            if map( lambda x:x[0], packed_str ) != str_def:
                output(t, None)
                total_count = None
                break
            else:
                for i in xrange( len(packed_str) ):
                    chars[i].append(packed_str[i][1])

        if total_count == None:
            continue

        for char_arr in chars:
            s = sum(char_arr)
            l = len(char_arr)
            m = s / l
            total_count += sum( [abs(x-m) for x in char_arr] )
        output(t, total_count)


if __name__ == "__main__":
   main()