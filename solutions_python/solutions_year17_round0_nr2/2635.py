import sys

def last_tidy_number(n):
    if len(n) <= 1: return n
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) < int(n[i - 1]):
            if i > 0:
                n = n[:i - 1] + "".join(str(int(n[i - 1]) - 1)) + "".join(['9' for i in range(i, len(n))])
            else:
                n = "".join(['9' for i in range(i, len(n))])
    return n if n[0] != '0' else n[1:]

def start(read_file, out_file):
    read = open(read_file, 'r')
    write = open(out_file, 'w')
    counter = -1
    for line in read:
        counter += 1
        if counter == 0: continue
        write.write("Case #" + str(counter).strip() + ": " + last_tidy_number(line.strip()) + '\n')
    read.close()
    write.close()

def main(argv):
    if len(argv) == 3:
        start(argv[1], argv[2])
        print("Done")
    else:
        print("Error with command line arguements\n")

main(sys.argv)