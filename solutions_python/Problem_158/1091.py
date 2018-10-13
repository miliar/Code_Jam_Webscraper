__author__ = 'Haewon'


# do the job
def main_job(x,r,c):
    #returns true when Richard can win

    if r > c:
        temp = c
        c = r
        r = temp

    if x >= 7:
        return True
    if (r*c)%x != 0:
        return True
    if c < x:
        return True
    if x == 2:
        return False
    if r <= x/2:
        return True

    return False


def main():
    #input read
    input_file = open("input1.in", 'rt')
    num_cases = int(input_file.readline())

    #output write
    output_file = open("output1.txt", 'w')

    for i in range(num_cases):
        line = input_file.readline()
        line = line.split()
        x = int(line[0])
        r = int(line[1])
        c = int(line[2])
        result = main_job(x,r,c)

        if result:
            output = "Case #%d: RICHARD\n" %(i+1)
        else:
            output = "Case #%d: GABRIEL\n" %(i+1)

        output_file.write(output)
        print(i+1)
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()