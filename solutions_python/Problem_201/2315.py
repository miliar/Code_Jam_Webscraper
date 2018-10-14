def make_stalls(N):
    s = ["1"]
    for _i in range(N):
        s.append("0")
    s.append("1")
    return "".join(s)


class Node:
    leftS = 0
    rightS = 0
    left = None
    right = None


def create_node(N):
    root = Node()
    if N % 2 == 1:
        root.leftS = N // 2
        root.rightS = root.leftS
    else:
        root.leftS = (N - 1) // 2
        root.rightS = N // 2
    return root


def insert_node(root):
    if root:
        # print("lS: %d rS: %d " % (root.leftS, root.rightS))
        if root.rightS > root.leftS:
            if root.right is None:
                root.right = create_node(root.rightS)
                root.rightS = max(root.right.leftS, root.right.rightS)
                return root.rightS, min(root.right.leftS, root.right.rightS)
            else:
                latestMax, latestMin = insert_node(root.right)
                root.rightS = max(root.right.rightS, root.right.leftS)
                return latestMax, latestMin
        else:
            if root.left is None:
                root.left = create_node(root.leftS)
                root.leftS = max(root.left.leftS, root.left.rightS)
                return root.leftS, min(root.left.leftS, root.left.rightS)
            else:
                latestMax, latestMin = insert_node(root.left)
                root.leftS = max(root.left.leftS, root.left.rightS)
                return latestMax, latestMin
    return 0, 0


def find_min_max(N, k):
    root_node = create_node(N)
    max_n = max(root_node.rightS, root_node.leftS)
    min_n = min(root_node.rightS, root_node.leftS)
    for i in range(1, k):
        max_n, min_n = insert_node(root_node)
    return max_n, min_n


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N, k = map(int, input().split(" "))
        print("Case #%d: %d %d" % ((i,) + find_min_max(N, k)))
