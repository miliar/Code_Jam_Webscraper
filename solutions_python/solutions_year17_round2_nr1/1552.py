__author__ = 'Haewon'


def cruise(d,position, speed):
    n = len(position)
    time = []
    for i in range(n):
        distance = d - position[i]
        time.append(distance/speed[i])

    max_time = max(time)

    return (d/max_time)

def matrix_to_string(matrix):
    m_string = ""
    for i in range(len(matrix)):
        m_row = matrix[i]
        m_row_string = ""
        for j in range(len(m_row)):
            m_row_string += m_row[j]
        m_row_string += "\n"
        m_string += m_row_string
    return m_string


def main():
    # # text input
    # input_file = open("input_a.txt", 'rt')
    # output_file = open("output_a.txt", 'w')

    # # small input
    # input_file = open("A-small.in", 'rt')
    # output_file = open("output_a_small.txt", 'w')
    #
    # large input
    input_file = open("A-large.in", 'rt')
    output_file = open("output_a_large.txt", 'w')


    num_cases = int(input_file.readline())

    for i in range(num_cases):
        line = input_file.readline()

        # input processing
        line = line.split()
        d = int(line[0])
        n = int(line[1])
        position = []
        speed =[]
        for j in range(n):
            line = input_file.readline()
            line = line.split()
            position.append(int(line[0]))
            speed.append(int(line[1]))

        # main function
        result = cruise(d, position, speed)

        # output processing
        output = "Case #%d: %.6f\n" %(i+1, result)
        output_file.write(output)

        print(i+1)

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()

