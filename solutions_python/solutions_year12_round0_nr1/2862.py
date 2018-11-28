constant_mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def read_file(s):
    input_handler = open(s, 'r')
    return input_handler.readlines()

def generate_result():   
    x = 30
    input_lines = read_file("A-small-attempt1.in")
    generate_mapping()
    for i,l in zip(input_lines, range(1, x+1)):
        temp = ""
        for k in i.strip():
            temp += constant_mapping[k]
        print "Case #%s: %s" % (l, temp)
        
def generate_mapping():
    mapping = dict()
    input_lines = read_file("trainning_set.txt")
    for i,j in zip(input_lines[0], input_lines[1]):
        mapping[j] = i
    print mapping
    return mapping


if __name__ == "__main__":
    generate_result()