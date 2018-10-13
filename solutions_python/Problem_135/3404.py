__author__ = 'phani'
import sys

def get_row(f):
    user_row_idx = int(f.readline()) - 1
    lines = [f.readline() for _ in xrange(4)]
    user_row = set([int(x) for x in lines[user_row_idx].split()])
    return user_row

def get_output(x, f):
    row1 = get_row(f)
    row2 = get_row(f)
    inter = row1.intersection(row2)
    output_line = ""

    if len(inter) == 1:
        output_line = "Case #%s: %s\n" % (x, list(inter)[0])
    elif len(inter) > 1:
        output_line = "Case #%s: Bad magician!\n" % (x,)
    elif len(inter) == 0:
        output_line = "Case #%s: Volunteer cheated!\n" % (x,)
    return output_line

def main():
    output = ""
    with open(sys.argv[1]) as f:
        t = int(f.readline())
        #print t
        for x in xrange(t):
            output += get_output(x+1, f)
    with open("output.txt", "wb") as f:
        f.write(output)

if __name__ == "__main__":
    main()
