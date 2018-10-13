import math

class BinaryTree():

    def __init__(self, capacity, parent, direction): # direction은 부모의 왼쪽 / 오른쪽 아들인지 알려주는 지표
        self.left = None
        self.right = None
        self.left_capa = math.floor((capacity-1) / 2)
        self.right_capa = math.ceil((capacity-1) / 2)
        self.parent = parent
        self.direct = direction

    def max(self):
        if self.left_capa >= self.right_capa:
            return self.left, self.left_capa, "left"
        else:
            return self.right, self.right_capa, "right"

    def update(self):
        current = self
        while(current.parent != None):
            max_capa = max(current.left_capa, current.right_capa)
            if(current.direct == "right"):
                current.parent.right_capa = max_capa
            else:
                current.parent.left_capa = max_capa
            current = current.parent

    def insert(self):
        current = self
        while(current != None):
            parent = current
            current, capa, direction = current.max()
        current = BinaryTree(capa, parent, direction)
        if direction == "right":
            parent.right = current
        else:
            parent.left = current
        current.update()
        return current.left_capa, current.right_capa


t = int(input())  # read a line with a single integer
F = open("bathroom-result.in", 'w')
for i in range(1, t + 1):
    numStall, numMan = input().split(" ")  # read a list of integers, 2 in this case
    numStall = int(numStall)
    numMan = int(numMan)

    stalls = BinaryTree(numStall, None, None)
    left = stalls.left_capa
    right = stalls.right_capa
    for man in range(numMan-1):
        left, right = stalls.insert()


    print("Case #{}: {} {}\n".format(i, max(left, right), min(left, right)))
    F.write("Case #{}: {} {}\n".format(i, max(left, right), min(left, right)))
    # check out .format's specification for more formatting options

F.close()