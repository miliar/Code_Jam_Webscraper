FILE = 'A-large.in'

def main():
    file = open(FILE).readlines()

    for i in range(1, len(file)):
        line = file[i].strip().split()

        n = int(line[1])
        stack = []
        flips = 0
            
        for o in line[0]:
            stack.append(o == '+')

        for c in range(len(stack)-n+1):
            if not stack[c]:
                for d in range(n):
                    stack[c+d] = not stack[c+d]

                flips += 1

        for c in stack:
            if not c:
                flips = 'IMPOSSIBLE'
                break

        print('Case #{}: {}'.format(i, flips))

main()
