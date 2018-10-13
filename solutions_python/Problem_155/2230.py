import sys

def file_loop():
    f = open(sys.argv[1])
    r = open(sys.argv[2], 'w')

    cnt = 0
    f.readline()
    for l in f:
        cnt += 1
        infos = l.strip().split(' ')
    
        result = main(infos[1])

        r.write('Case #%d: %d\n' % (cnt, result))

    f.close()
    r.close()


def main(shys):
    result = 0
    cur_sum = int(shys[0])
    for j in range(len(shys)):
        if shys[j] != '0' and cur_sum < j :
            result += j - cur_sum
            cur_sum += (j - cur_sum)

        if j != 0:
            cur_sum += int(shys[j])

    return result


if __name__ == "__main__":
    #print main('1100111')
    file_loop()
