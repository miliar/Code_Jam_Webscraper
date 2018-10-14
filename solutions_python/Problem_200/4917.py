def main():
    fh = open('B-small-attempt0.in', 'r')
    target = open('soultion.txt', 'w')
    n = 0
    next(fh)
    for line in fh.readlines():
        if tidy(line.strip()):
            n += 1
            target.write('Case #{}: {}'.format(n, line))
        else:
            while not tidy(line.strip()):
                line = str(int(line) - 1)
            n += 1
            target.write('Case #{}: {}\n'.format(n, line))

def tidy(N):
    num = []
    for i in N:
        num.append(int(i))
    if num == sorted(num):
        return True
    else:
        return False

if __name__ == '__main__': main()
