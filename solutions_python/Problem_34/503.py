import sys

def find_matches(pattern, set_list):
    result_set = False
    counter = 0
    in_brace = False
    for c in pattern:
        if c == '(':
            in_brace = True;
            item = set();
        elif c == ')':
            in_brace = False;
            if result_set == False:
                result_set = item
            else:
                result_set.intersection_update(item)
            counter += 1;
        else:
            if not set_list[counter].has_key(c):
                current_set = set()
            else:
                current_set = set_list[counter][c]
            if in_brace == True:
                item.update(current_set)
            else:
                if result_set == False:
                    result_set = current_set
                else:
                    result_set.intersection_update(current_set)
                counter += 1
    return result_set

def build_sets(letter_count, words):
    set_list = [dict() for i in range(letter_count)]
    word_len = len(words[0])
    for w in words:
        for c in range(word_len):
            if set_list[c].has_key(w[c]):
                set_list[c][w[c]].add(w)
            else:
                set_list[c][w[c]] = set()
                set_list[c][w[c]].add(w)
    return set_list


if __name__ == "__main__":
    input_file = sys.argv[1]
    data = open(input_file)
    (letter_count, word_count, case_count) = [int(i) for i in data.readline().strip().split()]
    words = []
    for i in range(word_count):
        words.append(data.readline().strip())
    set_list = build_sets(letter_count, words)
    for i in range(case_count):
        pattern = data.readline().strip()
        matches = find_matches(pattern, set_list)
        print "Case #%d: " % (i+1,) + str(len(matches))