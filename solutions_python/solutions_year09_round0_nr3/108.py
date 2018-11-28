from sys import stderr, stdout

how_many_cache = dict()
text = ""
pattern = "welcome to code jam"

# How many times the given pattern occurs in the given text?
def how_many(start_text, start_pattern):
    global how_many_cache
    global text
    global pattern

    #print >> stderr, "how_many(%s (%d), %s (%d))" % (text[start_text:], start_text, pattern[start_pattern:], start_pattern)

    if len(pattern) - start_pattern > len(text) - start_text:
        how_many_cache[(start_text, start_pattern)] = 0
        return how_many_cache[(start_text, start_pattern)]

    if start_pattern == len(pattern) - 1:
        how_many_cache[(start_text, start_pattern)] = text[start_text:].count(pattern[start_pattern:])
        return how_many_cache[(start_text, start_pattern)]

    sum = 0
    index = text.find(pattern[start_pattern], start_text)
    while index != -1:
        #print >> stderr, 'found character %s from index %d' % (pattern[start_pattern], index)
        if index + 1 < len(text):
            sum += how_many_cache[(index+1, start_pattern+1)]

        index = text.find(pattern[start_pattern], index + 1)

    how_many_cache[(start_text, start_pattern)] = sum % 10000
    return sum % 10000


def solve_case(case_text):
    global how_many_cache
    global text
    global pattern

    text = case_text
    how_many_cache = dict()

    #print >> stderr, len(text)
    #print >> stderr, len(pattern)

    for start_text in xrange(len(text)-1, -1, -1):
        for start_pattern in xrange(len(pattern)-1, -1, -1):
            res = how_many(start_text, start_pattern)
            #print >> stderr, "Result is %d" % res

    return how_many_cache[(0, 0)]


if __name__ == '__main__':
    # Read the input
    no_cases = int(raw_input(''))

    for case_ind in range(no_cases):
        text = raw_input('')

        #print >> stderr, text
        #print >> stderr, len(text)

        print >> stderr, "Solving case %d" % (case_ind + 1)

        sol = solve_case(text)

        stdout.write("Case #%d: " % (case_ind + 1))

        sol = sol % 10000
        if sol < 10:
            stdout.write("0")
        if sol < 100:
            stdout.write("0")
        if sol < 1000:
            stdout.write("0")
        stdout.write("%d\n" % sol)
