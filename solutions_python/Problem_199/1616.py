__author__ = 'Haewon'

__author__ = 'Haewon'


def pancakeFlip(p, k):
    num_flip = 0
    for i in range(len(p)):
        if p[i] == 0:
            flip_start = i
            flip_end = flip_start +k

            if (flip_end) > len(p):
                num_flip = -1
                return num_flip

            for j in range(flip_start, flip_end):
                p[j] = -p[j]+1

            num_flip += 1

    return num_flip

def main():
    #input read
    input_file = open("input_a_large.in", 'rt')
    num_cases = int(input_file.readline())

    #output write
    output_file = open("output_a_large.txt", 'w')

    for i in range(num_cases):
        line = input_file.readline()
        p=[]
        line = line.split()
        for ch in line[0]:
            if ch == '+':
                p.append(1)
            else:
                p.append(0)
        k = int(line[1])
        result = pancakeFlip(p, k)
        if result < 0:
            output = "Case #%d: IMPOSSIBLE\n" %(i+1)
        else:
            output = "Case #%d: %d\n" %(i+1, result)
        output_file.write(output)
        print(i+1)
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()