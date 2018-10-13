count = 0
end = False

def check(s, k):
    global count, end
    if all([i == '-' for i in s]):
        end = True
        if len(s) % k == 0:
            return count + len(s)/k
        return "IMPOSSIBLE"
    if all([i == '+' for i in s]):
        end = True
    return count

def flip(ss):
    return ''.join(['+' if i is '-' else '-' for i in ss])

def main():
    global count, end
    line_count = int(raw_input().strip())
    for z in xrange(line_count):
        line = raw_input().strip().split()
        s, k = line[0], int(line[1])
        count = 0
        end = False

        i, j = 0, len(s) - 1
        ret = check(s, k)
        if end:
            print "Case #%d:"%(z+1), ret
        else:
            while i < j:
                if s[i] == '-':
                    count += 1
                    s = s[:i] + flip(s[i:i+k]) + s[i+k:]
                    ret = check(s, k)
                if end:
                    break
                if s[j] == '-':
                    count += 1
                    s = s[:j-k+1] + flip(s[j-k+1:j+1]) + s[j+1:]
                    ret = check(s, k)
                if end:
                    break
                i += 1
                j -= 1
            if end:
                print "Case #%d:"%(z+1), ret
            else:
                print "Case #%d:" %(z+1), "IMPOSSIBLE"

if __name__ == '__main__':
    main()
