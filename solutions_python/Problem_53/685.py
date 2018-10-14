#!/usr/bin/env python

#def is_on(n, k):
 #   if k == 0:
  #      return "OFF"
   # if n > 1:
    #    clean = k - k % (2**(n - 1))
#        clean = clean / (2**(n - 1))
 #       return out(clean % 2)
  #  else:
   #     return out(k % 2)

def is_on(n, k):
    if k == 0:
        return "OFF"
    else:
        return out((k + 1) % 2**n)

def out(mod):
    if mod == 0:
        return "ON"
    else:
        return "OFF"
                                
if __name__ == "__main__":
    with open("/tmp/input", "r") as f:
        with open("/tmp/output", "w+") as g:
            t = int(f.readline())
            for i in xrange(t):
                header = f.readline().split()
                integers = [int(s) for s in header]
                g.write("Case #" + str(i + 1) + ": " + is_on(int(integers[0]), int(integers[1])) + "\n")
