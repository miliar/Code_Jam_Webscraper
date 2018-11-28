
def solve(num):
    #print('num:' +num)
    output = []
    for c in list(num):
        if not output or int(c) >= int(output[-1]):
            output.append(c)
        else: # c < output[-1]  : new < existing

            output[-1] = str(int(output[-1]) - 1)
            i = 2

            if len(output) > 1:
                while int(output[-1]) < int(output[-i]):
                    output[-i] = output[-1]
                    i += 1
                    # print(i)
                    # print(output)
                    if i > len(output) :
                        return neaten([output[0]] + ['9' for i in range(0, len(num)-1)])

            i = 1
            while len(output) > i and output[i-1] in ('0','9') and output[i] == '0':
                output[i] = '9'
                i += 1


            nines_to_add = len(num) - len(output)
            for i in range(0, nines_to_add):
                output.append('9')
            break

    return neaten(output)


def neaten(output):
    return ''.join([o for o in output if o != '0'])


assert int(solve('110'))== 99
assert int(solve('1100'))== 999
assert int(solve('111101'))== 99999
assert int(solve('100100100'))== 99999999

assert int(solve('885')) == 799

assert int(solve('12200'))== 11199

assert int(solve('1001'))== 999
assert int(solve('1992'))== 1889
assert int(solve('18898')) == 18889
assert int(solve('12254')) == 12249
assert int(solve('1225439')) == 1224999


if __name__ == '__main__':
    with file('B-small-attempt1.in') as f:
        _data = f.readline()
        _data = f.readline()
        i = 1
        while _data:
            num = _data.strip()
            print("Case #{x}: {y}".format(x=i, y=solve(num)))
            _data = f.readline()
            i += 1

