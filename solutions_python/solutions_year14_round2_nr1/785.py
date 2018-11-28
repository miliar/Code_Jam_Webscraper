#!/usr/bin/python
def min_moves(strings):    
    moves = 0
    for i in range(len(strings[0])):
        vals = []
        for string in strings:
            vals.append(string[i][1])
        avg = sum(vals) / len(vals)
        moves += sum(map(lambda x : abs(x - avg), vals))

    return moves

def passes_basic_tests(strings):
    length = len(strings[0])
    order  = "".join(map(lambda x : x[0], strings[0]))
    for string in strings:
        if not (length == len(string) and order == "".join(map(lambda x : x[0], string))):
            return False

    return True

def process(string):
    cur_letter_pos = -1
    ret = []
    for i in range(len(string)):
        if cur_letter_pos == -1:
            cur_letter_pos = i
        elif string[cur_letter_pos] == string[i]:
            continue
        else:
            ret.append((string[cur_letter_pos], i - cur_letter_pos))
            cur_letter_pos = i

    ret.append((string[cur_letter_pos], i - cur_letter_pos))

    #print string, ret
    return ret                    

def main():
    t = input()

    for i in range(1, t + 1):
        n = input()
        strings = []
        for j in range(n):
            s = raw_input().strip()
            strings.append(process(s))
        
        if passes_basic_tests(strings):
            v = min_moves(strings)
            print "Case #" + str(i) + ": " + str(v)
        else:
                print "Case #" + str(i) + ": Fegla Won"

if __name__ == "__main__":
    main()
