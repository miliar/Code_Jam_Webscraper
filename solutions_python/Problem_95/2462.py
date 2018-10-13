lang_map = {'y': 'a', 'q': 'z', 'e': 'o', 'z': 'q'}
googlerese_text = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
normal_text = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

for number in range(0, len(googlerese_text)):
    if(googlerese_text[number] not in lang_map):
        lang_map[googlerese_text[number]] = normal_text[number]

def process_file(file):
    f = open(file)
    text = f.read()
    f.close()
    lines = text.split('\n')
    return lines

def doit(input_string):
    output_string = ""
    for char in input_string:
        output_string += lang_map[char]
    return output_string
        
if __name__ == "__main__":
    filename = "a-small-attempt2.in"
    input_file = process_file(filename)
    t = input_file[0]
    for _t in range(1, len(input_file) - 1):
        answer = doit(input_file[_t])
        print("Case #%d: %s" % (_t, answer))
