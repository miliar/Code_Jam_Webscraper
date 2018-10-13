import sys
import StringIO


test = StringIO.StringIO("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
""")

def run(sequence):
    # sequence = [ (O,2), (b,1), (B,2) ]
    #print sequence
    button_number = 0
    time = 0
    state = { 'O': 1, 'B': 1 }
    while button_number < len(sequence):
        time += 1
        button = sequence[button_number]
        ### find the next button for the other robot
        for n in range(button_number+1, len(sequence)):
            next_button = sequence[n]
            if next_button[0] != button[0]:
                # this is the next button
                if state[next_button[0]] == next_button[1]:
                    # on the button
                    pass
                else:
                    # move it closer
                    if state[next_button[0]] > next_button[1]:
                        # go back
                        state[next_button[0]] -= 1
                    else:
                        state[next_button[0]] += 1
                break
        
        if state[button[0]] == button[1]:
            # push the button
            button_number += 1
        else:
            # move closer
            if state[button[0]] > button[1]:
                # go back
                state[button[0]] -= 1
            else:
                state[button[0]] += 1
    return time
        



try:
    infile = sys.argv[1]
    f = open(infile,'r')
    fo = open(infile + '.out', 'w')        
except IndexError:
    infile = 'test'
    f = test
    fo = sys.stdout

cases = int(f.readline().strip())
for casenum in range(cases):
    
    tokens = [x for x in f.readline().strip().split()]
    sequence = [(tokens[2*a+1],int(tokens[2*a+2])) for a in range(0, int(tokens[0]))]
    #print sequence

    res = run(sequence)
    
    fo.write('Case #%s: %s\n' % (1+casenum, res))
