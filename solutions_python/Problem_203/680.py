#!/usr/bin/python


def cake(lines):
    cpy_lines = lines
    for r in range(len(lines)):
        for i in range(len(lines[r])):
            if lines[r][i] == '?':
                # look for different ? in the current line 
                for j in reversed(range(0,i)):
                    if lines[r][j] != '?':
                        car = lines[r][j]
                        str_ = list(cpy_lines[r])
                        for k in range(j,i+1):
                            str_[k] = car
                            cpy_lines[r] = "".join(str_)
                            lines = cpy_lines
                        break


                for j in range(i, len(lines[r])):
                    if lines[r][j] != '?':
                        car = lines[r][j]
                        str_ = list(cpy_lines[r])
                        for k in range(i,j):
                            str_[k] = car
                            cpy_lines[r] = "".join(str_)
                            lines = cpy_lines
                        break

    for r in range(len(lines)):
        for i in range(len(lines[r])):
            if lines[r][i] == '?':
                # throw lines
                for j in reversed(range(0,r)):
                    if lines[j][i] != '?':
                        car = lines[j][i]
                        for k in range(j,r+1):
                            str_ = list(cpy_lines[k])
                            str_[i] = car
                            cpy_lines[k] = "".join(str_)
                            lines = cpy_lines
                        break

                for j in range(r,len(lines)):
                    if lines[j][i] != '?':
                        car = lines[j][i]
                        for k in range(r,j):
                            str_ = list(cpy_lines[k])
                            str_[i] = car
                            cpy_lines[k] = "".join(str_)
                            lines = cpy_lines
                        break



    # for r in range(len(lines)):


    #         find = False
    #         for j in range(0, len(lines)):
    #             if lines[j][i]!= '?':
    #                 car = lines[j][i]
    #                 for k in range(0,j):
    #                     str_ = list(cpy_lines[k])
    #                     str_[i] = car
    #                     cpy_lines[k] = "".join(str_)
    #                     find = True
    #         if not find:
    #             for j in reversed(range(0, i)):
    #                 if lines[0][j]!= '?':
    #                     car = lines[0][j]
    #                     str_ = list(cpy_lines[0])
    #                     for k in range(j,i):
    #                         str_[k] = car
    #                         cpy_lines[0] = "".join(str_)
    #                         find = True

    # lines = cpy_lines           

    # # rest
    # for i in range(1, len(lines)):
    #     for j in range(len(lines[i])):
    #         if lines[i][j] == '?':
    #             for k in reversed(range(0, i)):
    #                 if lines[k][j] != '?':
    #                     car = lines[k][j]
    #                     str_ = list(cpy_lines[i])
    #                     str_[j] = car
    #                     cpy_lines[i] = "".join(str_)
    #                     break

    return cpy_lines 


if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        input_ = raw_input("")
        r, c = str.split(input_, " ")
        r = int(r)
        c = int(c)
        lines = []
        for row in range(r):
            l = raw_input("")
            lines.append(l)
        cakes = cake(lines)
        print "CASE #{}:".format(test+1)
        for c in cakes:
            print c