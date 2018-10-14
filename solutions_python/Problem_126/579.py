import sys
import string

alphabets = string.ascii_lowercase
is_vowels_list = [bool(c in "aeiou") for c in alphabets]
is_vowels = dict(zip(alphabets, is_vowels_list))

def consec_conson(s):
    consec = False
    ret = 0
    cnt = 0
    for c in s:
        if not is_vowels[c]:
            if not consec:
                consec = True
            cnt += 1
        else:
            consec = False
            ret = max(ret, cnt)
            cnt = 0
    else:
        ret = max(ret, cnt)
    return ret


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        s, n_str = sys.stdin.readline().strip().split()
        l = len(s)
        n = int(n_str)
        ret = 0
        for i in range(l):
            for j in range(i+n, l+1):
                if consec_conson(s[i:j]) >= n:
                    ret +=1
        print "Case #%d: %d" % (t+1, ret)
