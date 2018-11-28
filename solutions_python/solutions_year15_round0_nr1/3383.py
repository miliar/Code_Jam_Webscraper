__author__ = 'gosu'

def main():
    f = open("input.in")

    count = 0
    for line in f:
        s = line.split()

        if len(s) > 1:
            audience = s[1]
            carry = 0
            results = 0
            for x in audience:
                current_shyness = int(x)
                if (current_shyness + carry) == 0:
                    results += 1
                else:
                    carry += current_shyness - 1

            print("Case #{}: {}".format(count, results))

        count += 1

if __name__ == '__main__':
    main()