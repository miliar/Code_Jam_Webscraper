def process_file(file):
    fsock = open(file)
    text = fsock.read()
    fsock.close()
    lines = text.split('\n')
    return lines
    
# define our method
def replace_all(text):
    a = 'abcdefghijklmnopqrstuvwxyz'
    #letters = string.ascii_lowercase
    x = 'yhesocvxduiglbkrztnwjpfmaq'
    result = ''
    for letter in text:
        try:
            position = a.index(letter)
            result += x[position]
        except:
            result += letter
    return result

    
def process_lines(lines):
    ans = []
    for cur in range(1, len(lines)-1):
        ans.append(replace_all(lines[cur]))
    return ans

if __name__ == "__main__":
    import sys, re, string
    filename = sys.argv[1]
    lines = process_file(filename)
    inp = process_lines(lines)
    for k, v in enumerate(inp):
        print "Case #%d: %s" % (k + 1, v)
