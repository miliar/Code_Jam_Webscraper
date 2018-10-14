import sys

__author__ = 'Gauthier'

def main(fd):
    lines = map(lambda x: x.strip(),fd.readlines())[1:]
    fd2 = open('output2.txt', 'w+')
    for j in range(len(lines)):
        l = lines[j]
        smax, people = l.split(' ')
        current_shyness = 0
        required_friend = 0
        for i in range(int(smax)+1):
            #print "{} people with shyness {} [{}]".format(people[i], i, current_shyness)
            if not int(people[i]):
                continue
            if current_shyness >= i:
                current_shyness += int(people[i])
            else:
                required_friend += (i - current_shyness)
                current_shyness += (i - current_shyness) + int(people[i])
        fd2.write("Case #{}: {}\r\n".format(j+1, required_friend))

if __name__ == "__main__":
    with open(sys.argv[1]) as fd:
        main(fd)