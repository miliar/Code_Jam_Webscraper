import sys


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    ifs = open(input_file, "r+")
    ofs = open(output_file, "w+")

    count = int(ifs.readline())

    for i in range(0, count):
        friends = 0
        total = 0
        line = ifs.readline()
        cp = int(line[0])
        for j in range(0, cp+1):

            inc = int(line[j+2])

            if total < j:
                rem = j - total
                friends += rem
                total += rem

            total += inc

        ofs.write("Case #"+str(i+1)+": "+str(friends)+"\n")


if __name__ == "__main__":
    main()
