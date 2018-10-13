def get_tidy(n):
    stack = [n[0]]
    back  = []
    n = n[1:]
    tidy = True
    length = len(n)

    for i in range(0, length):
        if tidy:
            next = n[i]
            top = stack.pop()

            if int(next) >= int(top):
                stack.append(top)
                stack.append(next)
            else:
                tidy = False

                backtrack = top

                while backtrack == top:
                    back.append(backtrack)

                    if len(stack) > 0:
                        backtrack = stack.pop()
                    else:
                        break

                if backtrack == top and len(stack) == 0:
                    if int(backtrack) - 1 != 0:
                        stack.append(str(int(backtrack) - 1))
                elif backtrack != top:
                    stack.append(backtrack)
                    b = back.pop()
                    if int(b) - 1 != 0:
                        stack.append(str(int(b) - 1))
                    else:
                        stack.append(b)
                    stack.append("9")

                while len(back) > 0:
                    stack.append("9")
                    back.pop()
        else:
            stack.append("9")

    return ''.join(stack)

t = int(raw_input())
for i in xrange(1, t + 1):
  n = raw_input()
  print "Case #{}: {}".format(i, get_tidy(n))