t = int(input())
count = 0


def split_segment(seg):
    h_seg = seg // 2
    if seg % 2 == 0:
        return h_seg, h_seg - 1
    else:
        return h_seg, h_seg


while t > 0:
    count += 1
    t -= 1
    n, k = input().split()
    n = int(n)
    k = int(k)

    max_y = -1
    min_y = -1
    segment = n
    while True:
        k -= 1
        r_seg, l_seg = split_segment(segment)

        if k == 0:
            max_y, min_y = r_seg, l_seg
            break

        if segment % 2 == 0:
            if k % 2 == 0:
                segment = l_seg
                k //= 2
            else:
                segment = r_seg
                k //= 2
                k += 1
        else:
            if k % 2 == 0:
                segment = r_seg
                k //= 2
            else:
                segment = l_seg
                k //= 2
                k += 1

    print("Case #{count}: {y} {z}".format(count=count, y=max_y, z=min_y))
