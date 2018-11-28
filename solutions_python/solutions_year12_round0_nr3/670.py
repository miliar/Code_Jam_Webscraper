def recycled_pairs(A,B):
    processed = set([])
    total = 0
    n_digits = len(str(A))

    def process(x):
        nonlocal total
        nonlocal processed
        num = 0
        x_str = str(x)
        for i in range(n_digits):
            x_str_rot = x_str[i:]+x_str[:i]
            x_rot = int(x_str_rot)
            if x_rot >= A and x_rot <= B and x_rot not in processed:
                num = num + 1
                processed.add(x_rot)
        if num >= 2:
            total = total + num*(num-1)//2

    for i in range(A,B):
        if i not in processed:
            process(i)

    return total
