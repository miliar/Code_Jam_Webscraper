def handle(t, s, p, ti):
    p = 3 * p
    out = 0
    for e in ti:
        if p - e <= 2:
            out += 1
        elif p - e <= 4 and e - (p-e) >= 0 :
            if s > 0:
                out += 1
                s -= 1
    return out


def main():
    fr = open('in.txt')
    fw = open('out.txt', 'w+')
    n = int(fr.readline())
    for i in range(1, n+1):
        line = fr.readline()
        nums = line.split(' ')
        t = int(nums[0])
        s = int(nums[1])
        p = int(nums[2])
        ti = [int(e) for e in nums[3:]]
        fw.write('Case #%d: %d\n'%(i, handle(t,s,p, ti)))
    fr.close()
    fw.close()

if __name__ == '__main__':
    main()
