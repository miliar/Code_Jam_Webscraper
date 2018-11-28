import sys


def alphabet_cake(cake):
    first_row_emtpy = False
    output = []
    for i,row in enumerate(cake):
        copy_char = '?'
        cur_pos = 0
        out_row = []
        while cur_pos < len(row) and row[cur_pos] == '?':
            if row[cur_pos] == '?':
                cur_pos = cur_pos + 1
        if row[0] == '?':
            if cur_pos == len(row):
                if i == 0:
                    first_row_emtpy = True
                    output.append([])
                    continue
                else:
                    # empty row, copy row above
                    out_row = output[i - 1]
                    output.append(out_row)
                    continue
            #print(row)
            #print(cur_pos)
            copy_char = row[cur_pos]
            out_row = [copy_char]*cur_pos
        # at least one char in row, start copy chars within row
        char_above = False
        char_below = False
        while cur_pos < len(row):
            if row[cur_pos] != '?':
                copy_char = row[cur_pos]
            #    stop_copy = False
            #   if char_below:
            #        if cake[i+1][cur_pos] != copy_char:
            #            stop_copy = True
            #    if char_above:
            #        if output[i-1][cur_pos] != copy_char:
            #            stop_copy = True
            #    if not stopy_copy:
            out_row.append(copy_char)
            # char_above = False
            # char_below = False
            # if i > 0 and output[i - 1][cur_pos] == copy_char:
            #   char_above = True
            #if i < len(cake) - 1 and cake[i + 1][cur_pos] == copy_char:
            #    char_below = True
            cur_pos = cur_pos + 1
        output.append(out_row)
    if first_row_emtpy:
        # copy next non empty row (must exist, otherwise empty cake)
        i = 1
        while len(output[i]) == 0:
            i = i+1
        for j in range(i):
            output[j] = output[i]
    return output


if __name__ == "__main__":
    name = "A-large"
    f = open("{0}.in".format(name))
    output = open("{0}.out".format(name), "w")
    cases = int(f.readline())
    for i in range(cases):
        split = f.readline().split()
        # print(split)
        R = int(split[0])
        C = int(split[1])
        cake = []
        for j in range(R):
            cake.append(list(f.readline().strip()))
        #print(cake)
        out_cake = alphabet_cake(cake)
        output.write("Case #" + str(i + 1) + ":\n")
        for row in out_cake:
            output.write(''.join(row) + '\n')
    f.close()
    output.close()
