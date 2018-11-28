def count(seq):
    seq = seq.split()
    blue_cur_pos = [1]
    orange_cur_pos = [1]
    secs = 0

    while seq:
        f_color = seq.pop(0)
        f_pos = int(seq.pop(0))

        if f_color == 'O':
            blue_pos = 0
            for i, l in enumerate(seq):
                if seq[i] == 'B':
                    blue_pos = int(seq[i+1])
                    break

            while len(orange_cur_pos) != f_pos:
                if len(orange_cur_pos) < f_pos:
                    orange_cur_pos.append(1)
                elif len(orange_cur_pos) > f_pos:
                    orange_cur_pos.pop()

                if len(blue_cur_pos) < blue_pos:
                    blue_cur_pos.append(1)
                elif len(blue_cur_pos) > blue_pos:
                    blue_cur_pos.pop()

                secs += 1
            secs += 1

            if len(blue_cur_pos) < blue_pos:
                blue_cur_pos.append(1)
            elif len(blue_cur_pos) > blue_pos:
                blue_cur_pos.pop()


        elif f_color == 'B':
            orange_pos = 0
            for i, l in enumerate(seq):
                if seq[i] == 'O':
                    orange_pos = int(seq[i+1])
                    break

            while len(blue_cur_pos) != f_pos:
                if len(blue_cur_pos) < f_pos:
                    blue_cur_pos.append(1)
                elif len(blue_cur_pos) > f_pos:
                    blue_cur_pos.pop()

                if len(orange_cur_pos) < orange_pos:
                    orange_cur_pos.append(1)
                elif len(orange_cur_pos) > orange_pos:
                    orange_cur_pos.pop()

                secs += 1
            secs += 1

            if len(orange_cur_pos) < orange_pos:
                orange_cur_pos.append(1)
            elif len(orange_cur_pos) > orange_pos:
                orange_cur_pos.pop()

    return secs


filename = 'A-large.in'
cases = []
num_cases = None
counter = 0
output = open('output', 'w')
for line in open(filename):
    if not num_cases:
        num_cases = line
    else:
        counter += 1
        sp = line.split()
        f_len = len(sp[0])
        f_len += 1
        result = count(line[f_len:])
        output.write('Case #' + str(counter) + ': ' + str(result)+'\n')

