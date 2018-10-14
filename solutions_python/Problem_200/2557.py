def get_answer(numb):
    pos = 1
    while pos < len(numb) and numb[pos] >= numb[pos - 1]:
        pos += 1
    if pos == len(numb):
        return numb
    else:
        sub_numb = numb[:pos]
        sub_numb[-1] -= 1
        return get_answer(sub_numb) + [9] * (len(numb) - pos)

with open('B-large.in') as inp, open('output.txt', 'w') as out:
    test_size = int(inp.readline())
    for test_num in range(1, test_size + 1):
        N = list(map(int, inp.readline().strip()))
        answer = int(''.join(map(str, get_answer(N))))
        out.write('Case #{}: {}\n'.format(test_num, answer))
