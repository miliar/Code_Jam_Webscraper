__author__ = 'michal'

import sys

def osmos(size, motes, moves):

    #print size, motes, moves

    if len(motes) == 0:
        return moves

    while motes[0] < size:
        first_mote = motes.pop(0)

        size += first_mote

        if len(motes) == 0:
            return moves

    # del
    #first_mote = motes.pop(0)
    #print "deleting", first_mote
    del_res = osmos(size, motes[1:], moves + 1)

    # add
    #motes.insert(0, first_mote)

    if size == 1:
        return del_res

    while motes[0] >= size:
        size += size - 1
        moves += 1

    add_res = osmos(size, motes, moves)


    return min(del_res, add_res)

if __name__=="__main__":

    file_out = None
    if len(sys.argv) >= 2:
        file = open(sys.argv[1])
        if len(sys.argv) == 3:
            file_out = open(sys.argv[2], 'w')
    else:
        file = sys.stdin

    cases = int(file.readline())

    for case in range(cases):

        line = file.readline()
        params = map(lambda x: int(x), line.split())

        initial = params[0]
        motes_num = params[1]

        line = file.readline()
        motes = map(lambda x: int(x), line.split())

        motes.sort()
        result = osmos(initial, motes, 0)

        out = "Case #%i: %s" % (case + 1, result)

        print out
        if file_out != None:
            file_out.write(out + '\n')



