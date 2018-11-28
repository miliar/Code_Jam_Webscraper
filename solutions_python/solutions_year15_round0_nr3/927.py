filename = "C-small-attempt0.in"
number = 0
case = 1
first_line = True
row_rules = {"11": "1", "1i": "i", "1j": "j", "1k": "k",
             "i1": "i", "ii": "-1", "ij": "k", "ik": "-j",
             "j1": "j", "ji": "-k", "jj": "-1", "jk": "i",
             "k1": "k", "ki": "j", "kj": "-i", "kk": "-1",
             "i": "i", "j": "j", "k": "k"}
with open("2015_c.out", "w") as f:
    for line in open(filename):
        line = line.strip()
        if not number:
            number = int(line)
        else:
            if first_line:
                b, rpt = line.split()
                first_line = False
            else:
                def gen(l, r):
                    for _ in range(r):
                        for ch in l:
                            yield ch
                str_len = len(line) * int(rpt)
                yes = False
                res = ""
                search = 0
                has_minus = False
                if str_len > 2:
                    current = ""
                    ind = 0
                    for s in gen(line, int(rpt)):
                        current += s
                        if len(current) > 2:
                            has_minus = True
                            current = current[1:]
                        else:
                            has_minus = False
                        if current in row_rules:
                            res = row_rules[current]
                        if has_minus:
                            if len(res) > 1:
                                res = res[1:]
                            else:
                                res = "-" + res
                        current = res
                        if search == 0 and res == "i":
                            search = 1
                            current = ""
                        elif search == 1 and res == "j":
                            search = 2
                            current = ""
                        elif search == 2 and res == "k" and ind == str_len - 1:
                            search = 3
                            current = ""
                        ind += 1
                if search == 3:
                    yes = True

                first_line = True

                f.write("Case #{0}: {1}\n".format(case, "YES" if yes else "NO"))
                print "Case #{0}: {1}".format(case, "YES" if yes else "NO")
                case += 1