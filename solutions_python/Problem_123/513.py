def num_moves(A, motes):
    new_motes = sorted(motes)
    while len(new_motes) > 0 and A > new_motes[0]:
        A += new_motes[0]
        new_motes = new_motes[1:]
    if len(new_motes) == 0:
        return 0
    elif A == 1:
        return len(new_motes)
    else:
        return 1+ min(num_moves(A, new_motes[1:]), num_moves(2*A-1, new_motes))

if __name__=='__main__':
    T = int(input())
    for i in range(T):
        Amotes = input().split()
        A,motes = int(Amotes[0]), int(Amotes[1])
        motes = input().split()
        motes = [int(mote) for mote in motes]
        print("Case #" + str(i+1) + ": " + str(num_moves(A, motes)))
