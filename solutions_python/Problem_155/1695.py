
import fileinput

inp = fileinput.input()

cases = int(inp.next()[:-1])
for case in range(cases):
    max_shyness, shyness = inp.next()[:-1].split(" ")
    max_missing = 0
    current = 0
    for i_shyness in range(int(max_shyness)+1):
        required = i_shyness
        max_missing = max([required - current, max_missing])
        current = current + int(shyness[i_shyness])
    print "Case #%d: %d" % (case+1, max_missing)