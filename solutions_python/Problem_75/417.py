def consume_next(vector, n=None):
    if n is None:
        value = vector[0]
        vector[0:1] = []
        return value
    else:
        elements = vector[:n]
        vector[:n] = []
        return elements


def solve_magicka(combinations, oppositions, elements):
    mapa = {}
    for (a, b, c) in combinations:
        mapa[a, b] = c
        mapa[b, a] = c

    op_set = set([(a, b) for (a, b) in oppositions])
    op_set |= set([(b, a) for (a, b) in oppositions])

    final_elements = []
    for element in elements:
        try:
            last = final_elements[-1]
            try:
                combined = mapa[last, element]
                final_elements[-1] = combined
            except KeyError:
                has_opposed = False
                for before in final_elements:
                    if (element, before) in op_set:
                        has_opposed = True
                if not has_opposed:
                    final_elements.append(element)
                else:
                    final_elements = []
        except IndexError:
            final_elements = [element]
    return str(final_elements).replace("'", "")


if __name__ == '__main__':
    number_of_tests = int(raw_input())
    for t in range(1, number_of_tests+1):
        test = raw_input().split(' ')
        c = int(consume_next(test))
        combinations = consume_next(test, c)
        d = int(consume_next(test))
        oppositions = consume_next(test, d)
        n = int(consume_next(test))
        elements = list(consume_next(test))
        answer = solve_magicka(combinations,
                               oppositions,
                               elements)
        print 'Case #%d: %s' % (t, answer)
