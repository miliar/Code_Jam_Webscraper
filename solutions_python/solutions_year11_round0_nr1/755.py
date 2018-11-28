# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
#----------^

#----------v
output = None
if len(sys.argv) == 3:
    output = open(sys.argv[2], 'w')
input = open(sys.argv[1])
#----------^

#----------v
for n in range(int(input.readline())):
#----------^
    o_pos = 1
    b_pos = 1
    seq = []
    _seq = input.readline().split()
    for i in range(int(_seq.pop(0))):
        seq.append((_seq.pop(0), int(_seq.pop(0))))
            
    result = 0
    while seq != []:
        o_init_pos = o_pos
        b_init_pos = b_pos
        if seq[0][0] == 'O':
            if o_pos < seq[0][1]:
                o_pos += 1
            if o_pos > seq[0][1]:
                o_pos -= 1
            for i in seq:
                if i[0] == 'B':
                    if b_pos < i[1]:
                        b_pos += 1
                    if b_pos > i[1]:
                        b_pos -= 1
                    break
        else:
            if b_pos < seq[0][1]:
                b_pos += 1
            if b_pos > seq[0][1]:
                b_pos -= 1
            for i in seq:
                if i[0] == 'O':
                    if o_pos < i[1]:
                        o_pos += 1
                    if o_pos > i[1]:
                        o_pos -= 1
                    break
        if (seq[0][0] == 'O' and o_pos == o_init_pos and o_pos == seq[0][1]) or \
          (seq[0][0] == 'B' and b_pos == b_init_pos and b_pos == seq[0][1]):
            seq.pop(0)
        result += 1
#----------v
    print("Case #"+str(n+1)+": "+str(result))
    if len(sys.argv) == 3:
        output.write("Case #"+str(n+1)+": "+str(result)+"\n")
if len(sys.argv) == 3:
    output.close()
#----------^










