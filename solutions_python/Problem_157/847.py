import itertools

def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))


def write_case(answer):
    w.write("Case #"+str(case_num+1)+": "+str(answer)+"\n")

mult = {
    "1": {
        "1": "1",
        "i": "i",
        "j": "j",
        "k": "k",
        "-1": "-1",
        "-i": "-i",
        "-j": "-j",
        "-k": "-k",
    },
    "i": {
        "1": "i",
        "i": "-1",
        "j": "k",
        "k": "-j",
        "-1": "-i",
        "-i": "1",
        "-j": "-k",
        "-k": "j",
    },
    "j": {
        "1": "j",
        "i": "-k",
        "j": "-1",
        "k": "i",
        "-1": "-j",
        "-i": "k",
        "-j": "1",
        "-k": "-i"
    },
    "k": {
        "1": "k",
        "i": "j",
        "j": "-i",
        "k": "-1",
        "-1": "-k",
        "-i": "-j",
        "-j": "i",
        "-k": "1"
    },
    "-1": {
        "1": "-1",
        "i": "-i",
        "j": "-j",
        "k": "-k",
        "-1": "1",
        "-i": "i",
        "-j": "j",
        "-k": "k"
    },
    "-i": {
        "1": "-i",
        "i": "1",
        "j": "-k",
        "k": "j",
        "-1": "i",
        "-i": "-1",
        "-j": "k",
        "-k": "-j"
    },
    "-j": {
        "1": "-j",
        "i": "k",
        "j": "1",
        "k": "-i",
        "-1": "j",
        "-i": "-k",
        "-j": "-1",
        "-k": "i"
    },
    "-k": {
        "1": "-k",
        "i": "-j",
        "j": "i",
        "k": "1",
        "-1": "k",
        "-i": "j",
        "-j": "-i",
        "-k": "-1"
    }
}

name = "C-small-attempt2"
f = file(name+".in")
w = file(name+".out", "w")
num_tests = int(f.readline().strip())
test_cases = split_seq(map(str.strip, f.readlines()),2)
f.close()

for case_num, case in enumerate(test_cases):
    sequence_length, num_repeats = map(int, case[0].split(" "))
    sequence = case[1]*num_repeats
    cur_num = "1"
    to_match = "i"
    for char in sequence:
        cur_num = mult[cur_num][char]
        if cur_num == to_match:
            if to_match == "i":
                to_match = "j"
            elif to_match == "j":
                to_match = "k"
            else:
                to_match = "f" #finished
            cur_num = "1"
            count = 0
            continue
    if cur_num == "1" and to_match == "f":
        write_case("YES")
    else:
        write_case("NO")


w.close()