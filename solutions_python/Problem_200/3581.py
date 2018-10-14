def last_tidy(ns):
    chars = [c for c in ns]
    while True:
        is_tidy = True
        for i in xrange(0, len(chars)-1):
            if int(chars[i]) > int(chars[i+1]):
                chars[i] = str(int(chars[i]) - 1)
                for j in xrange(i+1, len(chars)):
                    chars[j] = '9'
                is_tidy = False
                break
        if chars[0] == '0':
            chars = chars[1:]
        if is_tidy:
            break
    return "".join(chars)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  ns = raw_input()
  print "Case #{}: {}".format(i, last_tidy(ns))