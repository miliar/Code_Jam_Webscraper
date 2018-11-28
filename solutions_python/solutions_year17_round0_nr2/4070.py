def check(num):
    prev = 0
    for digit in str(num):
        if int(digit) < prev:
            return False
        prev = int(digit)
    return True


def main():
    output = ''
    input_file = open('B-small-attempt0.in', 'r')
    T = int(input_file.readline())
    for z in range(T):
        output += 'Case #' + str(z + 1) + ': '
        last_num = int(input_file.readline())
        tidy = last_num
        for i in range(last_num, 0, -1):
            if check(i):
                tidy = i
                break
        output += str(tidy) + '\n'
    outp = open('B-small-attempt0.out', 'w')
    outp.write(output)
    outp.close()
    # print(output)

if __name__ == '__main__':
    main()
