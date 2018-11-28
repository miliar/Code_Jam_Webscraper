def get_phone_number(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1

    int_as_str = ["ZERO", "TWO", "SIX", "EIGHT", "FOUR", "ONE", "THREE", "FIVE", "SEVEN", "NINE"]
    int_values = [0,2,6,8,4,1,3,5,7,9]
    slen = len(s)
    sl = slen
    i = 0
    number = []
    while sl:
        # print i, number, char_counts if i > 7 else {}
        ks = int_as_str[i]
        j = 0
        found = True
        for c in ks:
            if char_counts.get(c, 0):
                char_counts[c] -= 1
                sl -= 1
                j += 1
            else:
                break
        if j == len(ks):
            number.append(int_values[i])
            j = 0
        else:
            found = False
            for c in ks:
                if j > 0:
                    char_counts[c] = char_counts[c] + 1
                    sl += 1
                    j -= 1
                else:
                    break
        if not found:
            i += 1
    return ''.join(map(str, sorted(number)))
if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        s = raw_input()
        print "Case #{}: {}".format(i+1, get_phone_number(s))