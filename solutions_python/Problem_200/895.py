import sys

def solve(num_list):
    ans = []
    prev = 0
    nine = False
    for idx in range(len(num_list)):
        elem = num_list[idx]
        if nine:
            ans.append(9)
        elif elem >= prev:
            ans.append(elem)
            prev = elem
        else:
            nine = True
            convert(ans)
            ans.append(9)
    return int("".join(map(str, ans)))


def convert(arr):
    for x in range(len(arr)-1, -1, -1):
        if arr[x] > 0 and (x == 0) or (x != 0 and arr[x] != arr[x-1]):
            arr[x] = arr[x] - 1
            return
        else:
            arr[x] = 9
    raise ValueError("should not reach here")

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        val = sys.stdin.readline().strip()
        a_list = map(int, list(val))
        print "Case #{0}: {1}".format(case+1, solve(a_list))
