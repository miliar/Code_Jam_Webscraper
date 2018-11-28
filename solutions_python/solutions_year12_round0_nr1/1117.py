import sys

def build_translate_map():
    translate_map = {}

    from_letter = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z"
    to_letter = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q"

    for i in range(len(from_letter)):
        translate_map[from_letter[i]] = to_letter[i]

    return translate_map

def main():
    file_name = sys.argv[1]
    input_file = open(file_name, "r").readlines()
    translate_map = build_translate_map()
    test_cases = int(input_file[0])

    for j in range(1, test_cases + 1):
        letters = list(input_file[j])
        for i in range(len(letters)):
            replacement = translate_map.get(letters[i])
            if replacement:
                letters[i] = replacement
        translated = "".join(letters).strip()
        print "Case #%s: %s" % (j, translated)

if __name__ == "__main__":
    main()
