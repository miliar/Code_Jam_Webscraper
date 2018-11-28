import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def compute(string_in, n):
    seen_states = set()
    seen_states.add(string_in)
    target = '+'*len(string_in)

    cur_state = set()
    cur_state.add(string_in)
    count = 0
    while len(cur_state) > 0 and count < len(string_in):
        if target in cur_state:
            return count
        # print cur_state
        next_state = set()
        for string in cur_state:
            for j in xrange(len(string)-n+1):
                # print "str:",string
                new_str = string[:j]+string[j:j+n].replace('-', '.').replace('+', '-').replace('.', '+')+string[j+n:]
                # print "new str:",new_str
                if new_str not in seen_states:
                    seen_states.add(new_str)
                    next_state.add(new_str)
        cur_state = next_state
        count += 1

    return "IMPOSSIBLE"

def compute2(string_in, n):
    target = '+'*len(string_in)
    string = string_in
    count = 0
    for j in xrange(len(string_in) - n + 1):
        new_str = string
        if string[j] == '-':
            new_str = string[:j]+string[j:j+n].replace('-', '.').replace('+', '-').replace('.', '+')+string[j+n:]
            count += 1
        string = new_str

    if string == target:
        return count
    else:
        return "IMPOSSIBLE"

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    string, n = [s for s in raw_input().split(" ")]
    n = int(n)
    # print "Case #{}: {} {}".format(i, n + m, n * m)
    print "Case #{}: {}".format(i, compute2(string, n))
