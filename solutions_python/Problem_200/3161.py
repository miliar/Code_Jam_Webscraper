from contestio import GoogleCodeJam, NoParse


def main(ln):
    left = ln
    right_digits = []

    for i, (fst, snd) in enumerate(zip(ln, ln[1:])):
        if fst > snd:
            head_i = i
            for i_c in range(i - 1, -1, -1):
                if ln[i_c] == ln[i_c + 1]:
                    head_i = i_c
                else:
                    break
            head_c = ln[head_i]

            if head_c == '1':  # could not be 0
                pass
            else:
                right_digits.append(str(int(head_c) - 1))
            right_digits.extend('9' * (len(ln) - head_i - 1))

            left = ln[:head_i]
            break

    digits = []
    last = '0'
    for c in left:
        last = max(last, c)
        digits.append(last)

    digits.extend(right_digits)

    res = ''.join(digits) or '0'
    return res


if __name__ == '__main__':
    GoogleCodeJam().set(main, line_parser=NoParse()).run()
