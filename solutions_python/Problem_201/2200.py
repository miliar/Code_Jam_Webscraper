from bintrees import FastRBTree


def update_tree(tree, key):
    val = tree.get(key)
    if val is None:
        val = 1
    else:
        tree.remove(key)
        val += 1

    tree.insert(key, val)


def solve(n, k):
    tree = FastRBTree()
    tree.insert(n, 1)
    ls = rs = n

    for i in range(k):
        key, val = tree.max_item()
        tree.remove(key)

        if val > 1:
            tree.insert(key, val - 1)

        if key % 2 == 1:
            key //= 2
            ls = rs = key
            update_tree(tree, key)
            update_tree(tree, key)
        else:
            key //= 2
            ls = key
            rs = key - 1
            update_tree(tree, ls)
            update_tree(tree, rs)

    return str(ls) + " " + str(rs)


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = map(int, input().split(" "))
        print(f"Case #{i}: {solve(n, k)}")


if __name__ == "__main__": main()