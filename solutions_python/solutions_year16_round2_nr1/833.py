
def save_set(m, key, val):
    if val >= 0:
        m[key] = val

def save_get(m, key):
    try:
        return m[key]
    except KeyError:
        return 0

def save_decrease(m, key, decr):
    if decr > 0:
        m[key] = m[key] - decr

def decrease_all(m, number_str, num):
    for c in number_str:
        save_decrease(m, c, num)

def handle_number(number, number_str, char, counters, out):
    count = save_get(counters, char)
    decrease_all(counters, number_str, count)
    out[number] = count

def main():
    out = []
    for i in range(10):
        out.append(0)
    t = int(raw_input())
    for i in range(t):
        line = raw_input()
        counters = {}
        for c in line:
            count = save_get(counters, c)
            save_set(counters, c, count + 1)
        handle_number(2, 'TWO', 'W', counters, out)
        handle_number(4, 'FOUR', 'U', counters, out)
        handle_number(6, 'SIX', 'X', counters, out)
        handle_number(8, 'EIGHT', 'G', counters, out)
        handle_number(3, 'THREE', 'H', counters, out)
        handle_number(7, 'SEVEN', 'S', counters, out)
        handle_number(5, 'FIVE', 'V', counters, out)
        handle_number(9, 'NINE', 'I', counters, out)
        handle_number(1, 'ONE', 'N', counters, out)
        handle_number(0, 'ZERO', 'Z', counters, out)
        outstr = ''
        for k in range(10):
            for j in range(out[k]):
                outstr += str(k)
        print("Case #%i: %s" % (i + 1, outstr))

if __name__ == "__main__":
    main()
