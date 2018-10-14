__author__ = 'Haewon'


def tidyNumber(n):
    if len(n) == 1:
        result = list(map(str, n))
        result = ''.join(result)
        return result

    reverse_index = len(n)-1
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            reverse_index = i
            break

    if reverse_index == len(n)-1:
        result = list(map(str, n))
        result = ''.join(result)
        return result

    if reverse_index > 0:
        shift = 0
        reverse_number = n[reverse_index]-1
        for i in range(reverse_index):
            if n[reverse_index-i-1] <= reverse_number:
                break
            shift += 1
        reverse_index = reverse_index - shift

    n[reverse_index] = n[reverse_index]-1
    for i in range(reverse_index+1, len(n)):
        n[i] = 9

    if n[0] == 0:
        n.pop(0)
    result = list(map(str, n))
    result = ''.join(result)
    return result


def main():
    #input read
    input_file = open("input_b_large.in", 'rt')
    num_cases = int(input_file.readline())

    #output write
    output_file = open("output_b_large.txt", 'w')

    for i in range(num_cases):
        line = input_file.readline()
        n = []
        n.extend(line.rstrip())
        n = list(map(int, n))
        result = tidyNumber(n)
        output = "Case #%d: %s\n" %(i+1, result)
        output_file.write(output)
        print(i+1)
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()