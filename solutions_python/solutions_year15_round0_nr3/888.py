input = open("input.txt", "r")

cases = int(input.readline())

structure = [['1', 'i', 'j', 'k'],
             ['i', '-1', 'k', '-j'],
             ['j', '-k', '-1', 'i'],
             ['k', 'j', '-i', '-1']]

def get_index(letter):
    if letter == '1':
        return 0
    elif letter == 'i':
        return 1
    elif letter == 'j':
        return 2
    elif letter == 'k':
        return 3

def multiply_quaternions(a, b):
    negatives = 0
    if '-' in a:
        if '--' in a:
            negatives += 0
        else:
            negatives += 1
        a = a.replace('-', '')
    if '-' in b:
        if '--' in a:
            negatives += 0
        else:
            negatives += 1
        b = b.replace('-', '')
    product = structure[get_index(a)][get_index(b)]
    if (negatives % 2) == 1:
        if '-' in product:
            return product.replace('-', '')
        else:
            return '-' + product
    else:
        return product

with open('small_results.txt', 'w') as results:
    for case in range(cases):
        str_len, repeats = [int(x) for x in input.readline().split()]
        substring = input.readline().strip()
        test_string = substring * repeats
        got_i = False
        got_j = False
        got_k = False
        last_char = '1'
        for s_idx, character in enumerate(test_string):
            #print s_idx, last_char, character
            product = multiply_quaternions(last_char, character)
            if not got_i:
                if product == 'i':
                    last_char = '1'
                    got_i = True
                else:
                    last_char = product
            elif got_i and not got_j:
                if product == 'j':
                    last_char = '1'
                    got_j = True
                else:
                    last_char = product
            elif got_i and got_j and not got_k:
                if product == 'k' and s_idx == len(test_string)-1:
                    last_char = '1'
                    got_k = True
                else:
                    last_char = product
        if got_i and got_j and got_k:
            result = "YES"
        else:
            result = "NO"
        to_write = "Case #%i: %s" % (case+1, result)
        print to_write
        results.write(to_write + "\n")

input.close()