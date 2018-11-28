def is_tidy(num_str):
    prev = -1
    for i in num_str:
        cur = int(i)
        if  cur < prev:
            return False
        prev = cur
    return True

def prev_digit(d):
    if d == '0':
        return '9'
    return chr(ord(d) - 1)

def prev_tidy(inp):
    inp = list(inp)
    cur_pos = len(inp) - 1
    while not is_tidy("".join(inp)):
        inp[cur_pos] = '9'
        while True:
            inp[cur_pos-1] = prev_digit(inp[cur_pos-1])
            if inp[cur_pos-1] != '9':
                break
            cur_pos -= 1
        if cur_pos > 0:
            cur_pos -= 1
    return "".join(inp).lstrip('0')

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(0, n):
        inp = raw_input().strip()
        print "Case #%d: %s" % ( i + 1, prev_tidy(inp))
