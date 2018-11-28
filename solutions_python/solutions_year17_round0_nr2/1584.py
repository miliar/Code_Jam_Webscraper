import sys


def tidy(number):
    rev_number = list(reversed(number))
    last_nine = -1
    for i, digit in enumerate(rev_number):
        if i < len(number)-1:
            digit1 = int(rev_number[i])
            digit2 = int(rev_number[i+1])
            if digit1 < digit2:
                last_nine = i
                #print(rev_number)
                rev_number[i+1] = str(digit2-1)
                #print(rev_number)
                #print(last_nine)
    for j in range(last_nine+1):
        rev_number[j] = "9"
    res = list(reversed(rev_number))
    #print(res)
    #print(''.join(res).lstrip("0"))
    return int(''.join(res).lstrip("0"))


if __name__ == "__main__":
    name = "B-large"
    f = open("{0}.in".format(name))
    output = open("{0}.out".format(name), "w")
    cases = int(f.readline())
    for i in range(cases):
        num = list(f.readline().strip())
        #print(num)
        output.write("Case #" + str(i + 1) + ": " + str(tidy(num)) + "\n")
    f.close()
    output.close()
