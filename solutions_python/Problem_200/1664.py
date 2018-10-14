import sys

iname = sys.argv[1]
oname = iname.rstrip('in') + "out"
result = ""
with open(iname, "rb") as f:
    cases = int(f.readline().strip())
    for case in range(cases):
        line = f.readline().strip()
        result += "Case #%d: " % (case + 1)
        # only one number
        if len(line) == 1:
            result += line + "\n"
            continue
        length = len(line)
        i = length - 1
        while i > 0:
            c = line[i]
            cp = line[i - 1]
            if cp > c:
                line = str(int(line[:i]) - 1) + "9" * (length - i)
            i -= 1
        result += line.lstrip("0") + "\n"

with open(oname, "wb") as f:
    f.write(result)
