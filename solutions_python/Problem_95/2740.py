mapping = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
    'z': 'q'
}

def generate_mapping(original, translated):
    global mapping

    for i in xrange(len(original)):
        for j in xrange(len(original[i])):
            if not translated[i][j] in mapping:
                mapping[translated[i][j]] = original[i][j] 

def get_original_from_translation(translated_text):
    original = ""
    for c in translated_text:
        original += mapping[c]

    return original

if __name__ == "__main__":
    import sys

    translated = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    original = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

    generate_mapping(original, translated)

    # provide the original text given the translations
    num_of_cases = int(sys.stdin.readline().strip())
    output = ""

    for c in xrange(num_of_cases):
        translated_text = sys.stdin.readline().strip().lower()

        output += "Case #%d: %s\n" % (c+1, get_original_from_translation(translated_text))

    output = output.rstrip("\n")
    print output
