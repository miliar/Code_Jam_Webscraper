f = open('C-small.in')
message = "welcome to code jam"

def find(msg, text):
    total = 0
    if len(msg) == 1:
        return text.count(msg)
    if text == '':
        return 0
    for i, l in enumerate(text):
        if l == msg[0]:
            total += find(msg[1:], text[i+1:])
    return total

N = int(f.readline().strip())
for n in range(N):
    text = f.readline().strip()
    print "Case #%d: %04d" % (n+1, find(message, text))
