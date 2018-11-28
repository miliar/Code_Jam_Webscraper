def numEditsAbsorbMotes(mote_size, count, length):
    num_edits = 0
    if (count >= length):
        return 0
    if (mote_size == 1):
        return length - count
    if (mote_size <= blob_sizes[count]):
        if (2*mote_size-1 <= blob_sizes[count]):
            num_edits = min(numEditsAbsorbMotes(2*mote_size - 1, count, length),
                                numEditsAbsorbMotes(mote_size, count+1, length)) + 1
        else:
             num_edits = numEditsAbsorbMotes(2*mote_size-1, count, length) + 1
    else:
        num_edits = numEditsAbsorbMotes(mote_size + blob_sizes[count], count + 1, length)
    return num_edits

import sys
num_tests = int(sys.stdin.readline())
for test in xrange(1,num_tests+1):
    inp = sys.stdin.readline()
    inp = inp.split(' ')
    mote_size = int(inp[0])
    num_blobs = int(inp[1])
    blob_sizes = sys.stdin.readline()
    blob_sizes = blob_sizes.split(' ')
    blob_sizes = [int(it) for it in blob_sizes]
    blob_sizes.sort()
    del_needed = 0
    add_needed = 0
    print "Case #%d: %d"%(test, numEditsAbsorbMotes(mote_size, 0, num_blobs))  
