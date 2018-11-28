#!/usr/bin/python3
from sys import argv

def main(args):
    with open(args[1]) as inp, open(args[2], 'w') as out:
        cases = int(inp.readline())
        for case in range(cases):
            print('Case: ', case+1)
            n = int(inp.readline())
            words = []
            for scount in range(n):
                s = inp.readline()
                lst = tolist(s)
                words.append(lst)
            
            states = build_state(words)
            all_counts = 0
            if states == None:
                out.write('Case #%d: Fegla Won\n' % (case + 1))
            else:
                for (state, mid) in states:
                    count = 0
                    print (state)
                    for n in state:
                        count += abs(mid - n)
                    all_counts += count
                
                out.write('Case #%d: %d\n' % (case + 1, all_counts))
                

def build_state(words):
    states = [[]]

    for word in words:
        for i, pair in enumerate(word):
            if pair[0] == words[0][i][0]:
                if len(states) <= i:
                    states.append([pair[1]])
                else:
                    states[i].append(pair[1])
            else:
                return None
            
    mids = []
    for state in states:
        mids.append(sum(state) // len(state))

    return zip(states, mids)
           
def tolist(s):
    result = [[s[0], 1]]
    idx = 0
    for i, c in enumerate(s):
        if i != 0:
            if c == s[i - 1]:
                result[idx][1] += 1
            else:
                idx += 1
                result.append([c, 1])

    return result
        
if __name__ == '__main__':
    main(argv)
