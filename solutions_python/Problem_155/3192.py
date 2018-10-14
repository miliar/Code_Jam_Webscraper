def main():
    fi = 'A-large.in'
    fo = 'A-large.out'

    process_file(fi, fo)

def process_file(fin, fon):
    fi = open(fin)
    count = int(fi.readline()) # get counter at the first line
    output = ''

    for i in range(count):
        array_str = str_to_array(detach_word(fi.readline()))
        array = map(int, array_str)
        output += '\n' + 'Case #' + str(i+1) + ': ' +\
                    str(process_line(array))

    fo = open(fon, 'w')
    fo.write(output.strip())

    fi.close()
    fo.close()

def detach_word(s):
    word = ''
    for i in s:
        if i == '\n':
            return word
        elif i != ' ':
            word += i
        else:
            word = ''

def str_to_array(s):
    a = []
    for i in s:
        a.append(i)
    return a

def process_line(s):
    #pdb.set_trace()
    n = 0
    i = 1
    while i < len(s):
        sum_checked = sum_part(s[0:i])
        if s[i] != 0 and sum_checked < i:
            s[i-1] += i - sum_checked
            n += i - sum_checked
        i += 1
    return n

def sum_part(s):
    t = 0
    for i in s:
        t += i
    return t

if __name__ == '__main__':
    main()
