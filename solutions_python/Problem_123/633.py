def getMinimumSteps(motes, size):
    count = 0
    for mote in sorted(motes):
        if mote < size:
            size += mote

        elif mote < (2*size - 1):
            size += size - 1 + mote
            count += 1
        else:
            count += 1
    return count
        
def getMinimumStepsRec(motes, size):
    if not motes:
        return 0
    mote = motes[0]
    if mote < size:
        return getMinimumStepsRec(motes[1:], size+mote)
    if size == 1:
        return len(motes)
    return 1+min(getMinimumStepsRec(motes, 2*size-1), getMinimumStepsRec(motes[1:], size))

if __name__ == '__main__':
    import sys
    with sys.stdin as input:
        T = int(input.readline().strip())
        for i in range(T):
            x = input.readline().strip().split()
            size = int(x[0])
            N = int(x[1])
            x = input.readline().strip().split()
            motes = map(int, x)
            print "Case #%d: %d" %(i+1, getMinimumStepsRec(sorted(motes), size))
