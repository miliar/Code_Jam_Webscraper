import os
import sys

def magic(line, fPtr):
    tmp = {}
    
    tmp['card1'] = line
    rows = []
    rows.append(fPtr.next().strip().split(" "))
    rows.append(fPtr.next().strip().split(" "))
    rows.append(fPtr.next().strip().split(" "))
    rows.append(fPtr.next().strip().split(" "))
    tmp['rows1'] = rows
               
    tmp['card2'] = fPtr.next().strip()
    rows = []
    rows.append(fPtr.next().strip().split(" "))
    rows.append(fPtr.next().strip().split(" "))
    rows.append(fPtr.next().strip().split(" "))
    rows.append(fPtr.next().strip().split(" "))
    tmp['rows2'] = rows
    '''
    if tmp['card1'] == '':
        return 'Volunteer cheated!'
    elif tmp['card1'] == '':
        return 'Volunteer cheated!'
    elif len(tmp['card1'].split(" ")) > 1:
        return 'Bad magician!'
    elif len(tmp['card2'].split(" ")) > 1:
        return 'Bad magician!'
    '''
    
    row1 = tmp['rows1'][int(tmp['card1'])-1]
    row2 = tmp['rows2'][int(tmp['card2'])-1]
    
    res = list(set(row1)&set(row2))
    
    if len(res) > 1:
        return 'Bad magician!'
    
    if len(res) == 0:
        return 'Volunteer cheated!'
    
    return res[0]

def main(filename):
    with open(filename, 'r+') as f:
        pos = 0
        case_list = []
        cases = []
        try:
            for line in f:
                if pos == 0:
                    num_of_cases = line.strip()
                    pos += 1
                else:
                    print 'Case #'+str(pos)+': '+magic(line.strip(), f)
                    pos += 1

        except StopIteration:
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])