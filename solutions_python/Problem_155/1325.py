import sys

class Opera:
    __slots__ = ["max_energy", "shyness"]
    def __init__(self, seats):
        assert(len(seats) > 2)

        self.max_energy, stuff = seats.split(" ", 1)
        self.max_energy = int(self.max_energy)
        self.shyness = list(map(int, stuff))

def solve_opera(opera):
    activated_so_far = 0
    friends_to_invite = 0

    for i in range(len(opera.shyness)):
        if activated_so_far < i and opera.shyness[i] > 0:
            # we need to invite friends for this shyness level
            friends_to_invite += (i - activated_so_far)
            # we activate the current stage by including the added
            # friends, and those people with this shyness level
            activated_so_far  += (i - activated_so_far + opera.shyness[i])
        else:
            # we simply add these people to the activated
            activated_so_far += opera.shyness[i]

    return friends_to_invite

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage %s [filename]" % (sys.argv[0]))
        exit(1)
    filename = sys.argv[1]

    operas =  open(filename, "rt").read()

    number_of_sols, remainder = operas.split("\n", 1)

    opera_sols = [solve_opera(Opera(op)) for op in remainder.split("\n") if " " in op]

    assert(len(opera_sols) == int(number_of_sols))

    for k, sol in enumerate(opera_sols):
        print("Case #%d: %d" % (k+1, sol))
