f = open('B-large.in')
fw = open('B-large.out', 'w')

T = int(f.readline())
for t in xrange(T):
    N = f.readline().strip()
    curr = 0
    i_idx = -1
    is_valid = True
    for idx, digit_char in enumerate(N):
        digit = int(digit_char)
        if digit > curr:
            i_idx = idx
        if digit >= curr:
            curr = digit
        else:
            is_valid = False
            break

    fw.write('Case #' + str(t + 1) + ': ')
    if is_valid:
        fw.write(N + '\n')
    else:
        dec_num = int(N[0:i_idx + 1]) - 1
        dec_str = '' if dec_num == 0 else str(dec_num)
        new_str = dec_str + ('9' * (len(str(N)) - i_idx - 1))
        fw.write(new_str + '\n')

fw.close()
f.close()
