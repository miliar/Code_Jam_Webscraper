filename = "B-large.in"
rows = [i.strip() for i in file(filename).readlines()][1::]

i = 1


def calc(x):
    old_x = x
    y = get_print_line(x)
    while (y != old_x):
        print y
        old_x = y
        y = get_print_line(old_x)
    return y

def get_print_line(x):
    str_x = str(x)
    old = int(str_x[0])
    num = 0
    prefix = 1
    for i in str_x:
        ii = int(i)
        if ii < num % 10:
            #found
            prefix = 0
    
        num = num * 10
        num += ii * prefix
    return num-1 if prefix == 0 else num


with open("B-large.out", "w") as outf:
    for row in rows:
        s = int(row)
        outf.write("Case #" + str(i) + ": " + str(calc(s)) + "\n")
        i += 1


