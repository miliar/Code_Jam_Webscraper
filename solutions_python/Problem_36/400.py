#!/usr/bin/env python

PAT = 'welcome to code jam'

def solve(text):
    tbl = {}
    # create characters table
    for pos in range(len(text)):
        char = text[pos]
        if char in PAT:
            if tbl.has_key(char):
                tbl[char].append(pos)
            else:
                tbl[char] = [pos]

    return find_pattern(0, -1, tbl)

def find_pattern(start, min_index, tbl):
    if len(PAT[start:]) == 1:
        char = PAT[start]
        if not tbl.has_key(char):
            return 0
        else:
            count = 0
            for pos in tbl[char]:
                if pos > min_index:
                    count += 1
            return count
    else:
        if not tbl.has_key(PAT[start]):
            return 0
        else:
            count = 0
            for pos in tbl[PAT[start]]:
                if pos > min_index:
                    count += find_pattern(start+1, pos, tbl)
            return count
            
def main():
    n = int(raw_input())
    for case in range(n):
        text = raw_input()
        print 'Case #%d: %04d' % (case+1, solve(text))

if __name__ == '__main__':
    main()