import sys

def flip(pancakes, start_index, number):
    for i in range(start_index, start_index + number):
        if pancakes[i] == '-': pancakes[i] = '+'
        else: pancakes[i] = '-'
    return 1

def pancake_flipper(pancakes, k):
    flip_count = 0
    for i in range(0, len(pancakes) - k + 1):
        if pancakes[i] == '-': flip_count += flip(pancakes, i, k)
    if pancakes.count('-') == 0: return str(flip_count).strip()
    return "IMPOSSIBLE"

def start(read_file, write_file):
    read = open(read_file, 'r')
    write = open(write_file, 'w')
    counter = -1
    for line in read:
        counter += 1
        if counter == 0: continue
        write.write("Case #" + str(counter).strip() + ": " + pancake_flipper(list(line.split(' ')[0]), int(line.split(' ')[1])) + '\n')
    read.close()
    write.close()

def main(argv):
    if len(argv) == 3:
        start(argv[1], argv[2])
        print("Done")
    else:
        print("Error with command line arguements")

main(sys.argv)