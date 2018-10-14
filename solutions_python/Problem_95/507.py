import string

def translate(text):
    tr = 'ynficwlbkuomxsevzpdrjgthaq'
    table = string.maketrans(tr,string.ascii_lowercase,)
    return string.translate(text,table)


def main():
    inp = open('A-small.in', 'r')
    out = open('A-small.out', 'w')
    num_case = int(inp.readline())
    i = 1
    for line in inp:
        out.write("Case #"+str(i)+": "+translate(line))
        i+=1

if __name__ == "__main__":
    main()
