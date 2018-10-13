def occupy_room(left, right, occupied):
    """
    Recursive method that allows to place a person inside a room
    :param left: 
    :param right: 
    :param occupied: 
    :return: position, Ls, Rs or False, if person cannot be allotted a room
    """
    if left + 1 >= right:
        return False, False, False

    mid = int((left + right) / 2)

    if mid in occupied:
        if occupied[mid]:
            pos1, ls1, rs1 = occupy_room(left, mid, occupied)
            pos2, ls2, rs2 = occupy_room(mid, right, occupied)
            if not pos1:
                if pos2:
                    return pos2, ls2, rs2

            if not pos2:
                if pos1:
                    return pos1, ls1, rs1

            if ls1 > ls2:
                del occupied[pos2]
                return pos1, ls1, rs1
            elif ls1 == ls2:
                if rs1 >= rs2:
                    if pos2 in occupied:
                        del occupied[pos2]
                    return pos1, ls1, rs1
                else:
                    del occupied[pos1]
                    return pos2, ls2, rs2
            else:
                del occupied[pos1]
                return pos2, ls2, rs2

    else:
        occupied[mid] = True
        ls = mid - left - 1
        rs = right - mid - 1
        return mid, ls, rs


# oc = dict()
# oc[0] = True
# oc[7] = True
#
# pos1, ls1, rs1 = occupy_room(0, 7, oc)
# pos, ls, rs = occupy_room(0, 7, oc)
# print(pos)
# print(ls)
# print(rs)


def solve(N, K):
    occupied = dict()

    # The Guard rooms
    occupied[0] = True
    occupied[N + 1] = True

    for i in range(K):
        pos, ls, rs = occupy_room(0, N + 1, occupied)

    if ls >= rs:
        return str(ls) + " " + str(rs)
    else:
        return str(rs) + " " + str(ls)


if __name__ == '__main__':
    testcases = int(input())

    for nth_case in range(1, testcases + 1):
        N = input()
        N_str = N.split(" ")
        print("Case #%i: %s" % (nth_case, solve(int(N_str[0]), int(N_str[1]))))
