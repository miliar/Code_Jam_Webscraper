def process_file(file):
    f = open(file)
    text = f.read()
    f.close()
    lines = text.split('\n')
    return lines

def doit(a, b):
    recycled_numbers = list()
    for num in range(a, b + 1):
        number = num
        num_string = str(num)
        for _i in range(0, len(num_string) - 1):
            num_string = num_string[1:] + num_string[0]
            if(int(num_string) >= a and int(num_string) <= b and number < int(num_string)):
                #print((num, num_string))
                recycled_numbers.append((num, int(num_string)))
    return len(recycled_numbers)

if __name__ == "__main__":
    filename = "C-small-attempt0.in"
    input_file = process_file(filename)
    t = input_file[0]
    for _t in range(1, len(input_file) - 1):
        a, b = input_file[_t].split()
        answer = doit(int(a), int(b))
        print("Case #%d: %d" % (_t, answer))
