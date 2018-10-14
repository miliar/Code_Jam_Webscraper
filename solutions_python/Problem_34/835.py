DEBUG = False

def pr(str):
    if DEBUG:
        print(str)

def get_input():
    #return open("test.in")
    return open("A-small-attempt3.in")

def get_split_up(test_line):
    split_right = test_line.split(")")
    split_up = []
    for term in split_right:
        split_left = term.split("(")
        if split_left[0] != "":
            split_up.append((split_left[0], False))
        if len(split_left) == 2:
            split_up.append((split_left[1], True))
    return split_up

def do_logic(in_ptr, words):
    test_line = in_ptr.readline().strip()
    pr("test line: %s" % test_line)
    split_up = get_split_up(test_line)
    pr("split up: %s" % split_up)
    old_prefixes = [ "" ]
    old_words = dict(words)
    for chunk, regex in split_up:
        pr("\nProcessing chunk: %s %s" % (chunk, regex))
        prefixes_potential = []
        if regex:
            for char in chunk:
                prefixes_potential += [x+char for x in old_prefixes]
        else:
            prefixes_potential = [x+chunk for x in old_prefixes]
        pr("Potential prefixes newly constructed: %s" % prefixes_potential)
        new_words = {}
        new_prefixes = {}
        for word in old_words.keys():
            for prefix in prefixes_potential:
                if word.startswith(prefix):
                    new_words[word] = 1
                    new_prefixes[prefix] = 1
        old_words = new_words
        pr("Potential words left: %s" % new_words)
        old_prefixes = new_prefixes.keys()
        pr("Potential prefixes still valid: %s" % new_prefixes.keys())
        #raw_input()
    return len(new_words)

def print_result(case, result, out_ptr):
    print("Case #%s: %s" % (case, result))

def write_result(case, result, out_ptr):
    out_ptr.write("Case #%s: %s\n" % (case, result))

if __name__=="__main__":
    in_ptr = get_input()
    L, D, N = map(int, in_ptr.readline().split())
    words = {}
    for i in range(D):
        words[in_ptr.readline().strip()] = 1
    out_ptr = open("result.out", 'w')
    for i in range(N):
        word_copy = dict(words)
        result = do_logic(in_ptr, word_copy)
        #print_result(i+1, result, out_ptr)
        write_result(i+1, result, out_ptr)
    out_ptr.close()
