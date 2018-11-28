import sys

raw_input() # skip number of cases

msg = 'welcome to code jam'
msglen = len(msg)

def subsequences(input, input_offset=0, msg_offset=0):
    if done[(input_offset, msg_offset)] is not None:
        return done[(input_offset, msg_offset)]

    diff = len(input) - input_offset - (msglen - msg_offset)
    if diff < 0:
        done[(input_offset, msg_offset)] = 0
        return 0
    elif diff == 0:
        if input[input_offset:] == msg[msg_offset:]:
            done[(input_offset, msg_offset)] = 1
            return 1
        else:
            done[(input_offset, msg_offset)] = 0
            return 0

    count = subsequences(input, input_offset + 1, msg_offset)

    if input[input_offset] == msg[msg_offset]:
        if msg_offset == msglen - 1:
            count += 1
        else:
            count += subsequences(input, input_offset + 1, msg_offset + 1)

    done[(input_offset, msg_offset)] = count
    return count


for indx, line in enumerate(sys.stdin):
    done = {}
    for i in xrange(len(line)):
        for msgindx in xrange(msglen):
            done[(i, msgindx)] = None
    count = subsequences(line)
    print 'Case #%d: %s' % (indx + 1, str(count)[-4:].zfill(4))
