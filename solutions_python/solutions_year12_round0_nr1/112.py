if __name__ == '__main__':
    f = open('A-small-attempt0.in')
    output = open('A-small-attempt0.out', 'w')
    test_case = int(f.readline())
    code_dict = {'a': 'y', 'b': 'h', 'c': 'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n' : 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u' : 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z':'q', ' ': ' '}
    for i in range(test_case):
        line = f.readline()
        line = line.strip()
        out_str = ''
        for char in line:
            out_str += code_dict[char]
        s = 'Case #%s: ' %(i+1)
        output.write(s + out_str + '\n')
    output.close()
    f.close()
