enter = 1
backspace = 1

def ev_finish(typed, pass_len, probs):
    "typed is int, pass_len is int, probs is list of probabilities. Return expected val if finish"
    # if finish is P(all correct)*pass_len + P(not all correct)*(pass_len + enter + pass_len + enter)
    p=1
    for i in range(typed):
        p *= probs[i]
    return (p*(pass_len - typed + enter) + (1-p)*(pass_len-typed+enter+pass_len+enter))

def ev_backspace(typed, pass_len, probs, x):
    # let x be the number of spaces backspaced
    # ev is typed + x*backspace + P(all up to typed-x correct)*(pass_len-typed+x+enter)
    #  + P(at least one from 0 to typed-x is incorrect)*(pass_len-typed+x+enter+pass_len+enter)
    start = typed-x
    p=1
    for i in range(start):
        p *= probs[i]
    print p
    return (x*backspace + p*(pass_len-start+enter) + (1-p)*(pass_len-start+enter+pass_len+enter))

def ev_enter(typed, pass_len, probs):
    # ev is typed+enter+pass_len+enter
    return (enter+pass_len + enter)

def get_best_ev(typed, pass_len, probs):
    c = [ev_backspace(typed, pass_len, probs, x) for x in range(typed+1)]
    c.append(ev_finish(typed, pass_len, probs))
    c.append(ev_enter(typed, pass_len, probs))
    print c
    return min(c)

def read_input_file(filename = "A-small-attempt0.in"):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    N = int(lines[0])
    cases = lines[1:]
    return N, cases

def create_output(answers, filename = "Asolution.txt"):
    file = open(filename, 'w')
    for i in range(len(answers)):
        print "Case #%d: %s" % (i+1, answers[i])
        output = "Case #%d: %s\n" % (i+1, answers[i])
        file.write(output)
    file.close()

T, cases = read_input_file()
bests = []

for i in range(T):
    a = cases.pop(0).split()
    b = cases.pop(0).split()
    print cases
    print a, b
    typed, pass_len = (int(a[0]), int(a[1]))
    probs = [float(probability) for probability in b]
    bests.append(get_best_ev(typed, pass_len, probs))

create_output(bests)