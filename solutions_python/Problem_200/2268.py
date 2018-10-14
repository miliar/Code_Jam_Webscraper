def test_tidy(x):
    last = None
    for c in str(x):
        if last is None:
            last = c
            continue
        if int(c) < int(last):
            return False
        last = c
    return True

f = open('input', 'r')
tests = int(f.readline())
for i in range(tests):
    line = f.readline().rstrip()
    val = int(line)
    mask = 1
    while not test_tidy(val):
        cut = (val // mask) % 10
        val -= mask if cut == 0 else (cut+1)*mask
        mask *= 10
    print("Case #"+str(i+1)+": "+str(val))


