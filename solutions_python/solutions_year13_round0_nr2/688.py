import pprint
import string
import sys

def read_lawn(in_fd, r, c):
    lawn = []
    for i in range(r):
        int_list = map(int, in_fd.readline().strip().split())
        lawn.append(int_list)
    pprint.pprint(lawn)
    return lawn

def containsOnly(li, chars):
    for c in li:
        if not c in chars:
            return False
    return True

def getCol(lawn, c):
    return [lawn[r][c] for r in range(len(lawn))]

def mowLawnAtHeight(lawn, m_lawn, height):
    for c, (t_h, b_h) in enumerate(zip(lawn[0], lawn[-1])):
        if (t_h == height or b_h == height) and isMowable(lawn, height, c, 's'):
            mowCol(m_lawn, height, c)
    for r, (t_h, b_h) in enumerate(zip(getCol(lawn, 0), getCol(lawn, len(lawn[0]) - 1))):
        if (t_h == height or b_h == height) and isMowable(lawn, height, r, 'e'):
            mowRow(m_lawn, height, r)

def mowCol(m_lawn, height, c):
    for r in range(len(m_lawn)):
        m_lawn[r][c] = min(m_lawn[r][c], height)
def mowRow(m_lawn, height, r):
    for c in range(len(m_lawn[0])):
        m_lawn[r][c] = min(m_lawn[r][c], height)

def areLawnsIdentical(lawn, mowed_lawn):
    print 'comparing'
    pprint.pprint(lawn)
    pprint.pprint(mowed_lawn)
    for r in range(len(lawn)):
        for c in range(len(lawn[0])):
            if lawn[r][c] != mowed_lawn[r][c]:
                return False
    return True

def isMowable(lawn, height, index, direction):
    print 'trying to mow height: ', height, index, direction
    if direction == 's':
        for r in range(len(lawn)):
            if height < lawn[r][index]:
                print "can't mow", r, index
                return False
        return True
    elif direction == 'e':
        for c in range(len(lawn[0])):
            if height < lawn[index][c]:
                print "can't mow", index, c
                return False
        return True
    else:
        print "error start_r or start_c"
        sys.exit(1)

def mowLawn(lawn, mowed_lawn, height, index, direction):
    print 'trying to mow height: ', height, index, direction
    if direction == 's':
        for r in range(len(lawn)):
            if mowed_lawn[r][index] < height:
                print "can't mow", r, index
                return False
            mowed_lawn[r][index] = height
        pprint.pprint(mowed_lawn)
        print 'mowed'
        return True
    elif direction == 'e':
        for c in range(len(lawn[0])):
            if mowed_lawn[index][c] < height:
                print "can't mow", index, c
                return False
            mowed_lawn[index][c] = height
        pprint.pprint(mowed_lawn)
        print 'mowed'
        return True
    else:
        print "error start_r or start_c"
        sys.exit(1)

def can_mow(lawn):
    max_h = 100
    mowedPaths = set()
    mowed_lawn = []
    for r in range(len(lawn)):
        mowed_lawn.append([max_h] * len(lawn[0]))
    min_height = max_h
    for row in lawn:
        for h in row:
            min_height = min(min_height, h)

    for height in range(max_h - 1, min_height - 1, -1):
        mowLawnAtHeight(lawn, mowed_lawn, height)
    return areLawnsIdentical(lawn, mowed_lawn)

def main(in_fd, out_fd):
    n = int(in_fd.readline())
    for i in range(n):
        r, c = map(int, in_fd.readline().strip().split())
        lawn = read_lawn(in_fd, r, c)
        write_output(out_fd, i, 'YES' if can_mow(lawn) else 'NO')

def write_output(out_fd, i, output):
    out_fd.write('Case #{0}: {1}\n'.format(i + 1, output))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Need file name"
        sys.exit(1)
    in_name = sys.argv[1]
    out_name = string.replace(in_name, ".in", ".out")
    with open(in_name) as in_fd:
        with open(out_name, 'w') as out_fd:
            main(in_fd, out_fd)
