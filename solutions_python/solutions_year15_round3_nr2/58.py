def solve(keys, word, s):
    def count(buf):
        ret = 0
        for i in range(len(buf)):
            if ''.join(buf[i:i + len(word)]) == word:
                ret += 1
        return ret
    def iter(i, buf):
        if i == s:
            v = count(buf)
            return (v, v)
        ret_sum, ret_max = 0, 0
        for key in keys:
            buf[i] = key
            c_sum, c_max = iter(i + 1, buf)
            ret_sum += c_sum
            ret_max = max(ret_max, c_max)
        return (ret_sum, ret_max)
    r_sum, r_max = iter(0, [' '] * s)
    na = len(keys) ** s
    return 1.0 * (r_max * na - r_sum) / na

if __name__ == '__main__':
    tc = int(raw_input())
    for cc in range(tc):
        [nk, l, s] = [int(x) for x in raw_input().split()]
        keys = raw_input().strip()
        word = raw_input().strip()
        print 'Case #%d: %.7f' % (cc + 1, solve(keys, word, s))
