def run():
    loop = input()
    for i in range(int(loop)):
        problem = input()
        cakes, flipper = problem.split()
        flipper = int(flipper)
        answer = solve(cakes, flipper)
        write(answer, i)

def solve(cakes, flipper):
    counter = 0
    idx = cakes.find('-')
    while(idx != -1 and counter < len(cakes)):
        counter += 1
        sub_cakes = cakes[idx:idx+flipper]
        if len(sub_cakes) < flipper:
            continue
        else:
            sub_cakes = sub_cakes.replace('+', 'h')
            sub_cakes = sub_cakes.replace('-', 'e')
            sub_cakes = sub_cakes.replace('e', '+')
            sub_cakes = sub_cakes.replace('h', '-')
            cakes = cakes[:idx] + sub_cakes + cakes[idx+flipper:]
            idx = cakes.find('-')

    return counter if counter < len(cakes) else 'IMPOSSIBLE'

def write(answer, i):
    print('Case #{i}: {answer}'.format(answer=answer, i=(i+1)))


if __name__ == '__main__':
    run()
