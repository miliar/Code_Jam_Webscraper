
def result(text):
    nums = [int(i) for i in text.split()]
    S = nums[1]
    p = nums[2]
    t = nums[3:]
    t.sort(reverse=True)
    for i,ti in enumerate(t):
        if ti >= p*3:
            continue
        elif ti >= p*3-2 and p>0:
            continue
        elif S and ti >= p*3-4 and p>1:
            S -= 1
            continue
        else:
            i -= 1
            break
    return i+1

def solve(filename='sample.in'):
    fi = open(filename)
    fo = open(filename+'.out', 'w')
    N = int(fi.readline().strip())
    for i,line in enumerate(fi):
        line = line.rstrip('\n')
        wr = 'Case #%d: %s'%(i+1, result(line))
        print line
        print wr
        if i != N-1:
            wr += '\n'
        fo.write(wr)
    fo.close()
    fi.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv)>1:
        solve(sys.argv[1])
    else:
        solve()
