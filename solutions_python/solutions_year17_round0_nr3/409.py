import sys

def debug(line):
    sys.stderr.write(line + "\n")
    return

def info(line):
    sys.stderr.write(line + "\n")
    return

# class node:
#     start = -1
#     end = -1
#     isRight = False
#     left_node = None
#     right_node = None
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         left_node = None
#         right_node = None
#
#     def get_len(self):
#         return (self.end - self.start)
#
#     def get_next(self):
#         if self.get_len() == 1:
#             return 0, 0, self.start
#
#         if self.left_node is None and self.right_node is None:
#             mid = (self.start + self.end - 1) / 2
#             self.left_node = node(self.start, mid)
#             self.right_node = node(mid + 1, self.end)
#             self.isRight = self.get_len() % 2 == 0
#             Ls = self.left_node.get_len()
#             Rs = self.right_node.get_len()
#             # debug("return myself mid...i'm: {} ~ {}".format(self.start, self.end))
#             return Ls, Rs, mid
#         elif self.isRight == True:
#             # debug("ask my right: {} ~ {}".format(self.right_node.start, self.right_node.end))
#             self.isRight = False
#             return self.right_node.get_next()
#         else:
#             # debug("ask my left: {} ~ {}".format(self.left_node.start, self.left_node.end))
#             self.isRight = True
#             return self.left_node.get_next()

class node:
    start = -1
    end = -1
    mid = -1
    isRight = False
    left_node = None
    right_node = None

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (self.start + self.end - 1) / 2

        self.isRight = self.get_len() % 2 == 0


    def get_len(self):
        return (self.end - self.start)

    def get_ans(self, target):
        debug("find anser in {} ~ {} after {}".format(self.start, self.end, target))
        if target == 1:
            self.left_node = node(self.start, self.mid)
            self.right_node = node(self.mid + 1, self.end)
            Ls = self.left_node.get_len()
            Rs = self.right_node.get_len()
            debug("return answer: ls: {}, rs: {}, mid: {}".format(Ls, Rs, self.mid))
            return Ls, Rs, self.mid

        if self.isRight:
            if target % 2 == 0:
                self.right_node = node(self.mid + 1, self.end)
                return self.right_node.get_ans(target / 2)
            else:
                self.left_node = node(self.start, self.mid)
                return self.left_node.get_ans(target / 2)
        else:
            if target % 2 == 0:
                self.left_node = node(self.start, self.mid)
                return self.left_node.get_ans(target / 2)
            else:
                self.right_node = node(self.mid + 1, self.end)
                return self.right_node.get_ans(target / 2)

def find_ans(n, k):
    parent_node = node(0, n)
    Ls = 0
    Rs = 0
    mid = 0

    # occupied = ['.' for x in range(n + 2)]
    # occupied[0] = 'O'
    # occupied[n + 1] = 'O'

    # for i in range(0, k):
    #     Ls, Rs, mid = parent_node.get_next()
        # debug("#{} is at {}".format(i, mid))

        # occupied[mid + 1] = 'O'
        # debug("#{0:4}: {1}".format(i, "".join(occupied)))

    Ls, Rs, mid = parent_node.get_ans(k)
    max = Ls if Ls > Rs else Rs
    min = Ls if Ls < Rs else Rs

    return max, min

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    info("Solving Case #{}: {} {}".format(i, n, k))

    ans_max, ans_min = find_ans(n, k)

    print "Case #{}: {} {}".format(i, ans_max, ans_min)
    # check out .format's specification for more formatting options