for TC in range(1, int(raw_input()) + 1):
    n, x = map(int, raw_input().split())
    files = sorted(map(int, raw_input().split()), reverse=True)
    disks = 0
    while files:
        if len(files) == 1:
            disks += 1
            files.pop()
        else:
            if files[0] + files[-1] <= x:
                i = len(files) - 1
                while files[0] + files[i] <= x:
                    if i == 1:
                        biggest = i
                        break
                    else:
                        biggest = i
                        i -= 1
                files.pop(biggest)
                files.pop(0)
                disks += 1
            else:
                files.pop(0)
                disks += 1
    print "Case #%d: %d" % (TC, disks)
            