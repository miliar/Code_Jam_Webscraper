def get_time(rate, target, offset):
    return target/rate + offset

def cookie_clicker_alpha(filename):
    fin = open(filename, 'r')
    out = open('cookie_clicker_alpha.out', 'w')
    cases = int(fin.readline())
    case = 1
    while case <= cases:
        nums = map(lambda n: float(n), fin.readline().replace('\n','').split(' '))
        c = nums[0]
        f = nums[1]
        x = nums[2]

        best_time = 0
        rate = 2
        offset = 0
        while True:
            next_rate = rate + f
            next_offset = c / rate + offset
            best_time = get_time(rate, x, offset)
            next_time = get_time(next_rate, x, next_offset)
            if next_time < best_time:
                rate = next_rate
                offset = next_offset
                best_time = next_time
            else:
                break
        out.write('Case #%d: %.7f\n' % (case, best_time))


        case+=1

    fin.close()
    out.close()


cookie_clicker_alpha('B-large.in')