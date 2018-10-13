tc = int(input())

def back_track(curr_idx, next_idx, inte):
    inte[curr_idx] -= 1
    pivot = curr_idx
    for idx in range(curr_idx, -1, -1):
        if inte[curr_idx] < inte[idx]:
            pivot = idx

    return pivot


for c in range(tc):
    number = int(input())
    inte = list(map(int, str(number)))
    length = len(inte)
    full = number
    for idx, el in enumerate(inte):

        if idx+1 == length:
            break

        nex = inte[idx+1] 
        curr = el

        if nex < curr:
            pivot = back_track(idx, idx+1, inte)

            selisih = length - pivot - 1
            power = 10 ** selisih
            head = number // power
            full = head * power - 1

            break
    print("Case #{0}: {1}".format(c+1, full))