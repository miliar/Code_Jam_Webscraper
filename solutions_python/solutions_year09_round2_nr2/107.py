def next_permutation(seq, pred=cmp):
    def reverse(seq, start, end):
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
            
    last = len(seq)
    seq = seq[:]
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1
        while True:
            current = next
            next -= 1
            if pred(seq[next], seq[current]) < 0:
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                reverse(seq, current, last)
                yield seq[:]
                break
            if next == 0:
                raise StopIteration
    raise StopIteration

def next_val(n):
    iter = next_permutation(list(str(n)))
    try:
        return int(''.join(iter.next()))
    except:
        smallest_nonzero = sorted(str(n).replace('0', ''))[0]
        smallest_nonzero_omitted = str(n).replace(smallest_nonzero, '', 1)
        lex = sorted(smallest_nonzero_omitted)
        return int(''.join([smallest_nonzero,'0'] + lex))

def main():
    infile = open('B-large.in')
    outfile = open('B-large.out', 'w')
    num_cases = int(infile.readline())
    for i in xrange(num_cases):
        n = int(infile.readline())
        print n
        output = 'Case #%d: %s\n'%(i+1, next_val(n))
        print output,
        outfile.write(output)
    outfile.close()
               
if __name__ == '__main__':
    main()
    