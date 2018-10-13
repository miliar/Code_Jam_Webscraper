
def my_split(expression, length):
    ret_val = []
    buf = ''

    for char in expression:
        if char.isalpha():
            if buf:
                buf += char
            else:
                ret_val.append(char)
        elif char == '(':
            buf = char
        elif char == ')':
            ret_val.append(buf[1:])
            buf = ''
        else:
            raise ValueError
    assert(len(ret_val) == length)
    return ret_val

def main():
    L, D, N = map(int, raw_input().split())

    known_words = [raw_input() for x in xrange(D)]
    for case in xrange(N):
        expression = my_split(raw_input(), L)
        counter = 0
        for word in known_words[:]:
            for i in xrange(len(word)):
                if word[i] not in expression[i]:
                    break
            else:
                counter += 1

        print 'Case #%d: %d' % (case + 1, counter)

if __name__ == '__main__':
    main()
