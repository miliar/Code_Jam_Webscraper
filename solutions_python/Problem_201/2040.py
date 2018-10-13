class Stalls(object):

    def __init__(self, n):
        self.N = n
        self.middle = None

    def get_indexes(self, n):
        half  = n//2
        rest = n % 2

        if rest == 0:
            l = half -1
        else:
            l = half

        r = half

        return half + rest, l, r

    def add_people(self, p):
        if self.middle == None:
            # First person
            i, l, r = self.get_indexes(self.N)
            self.middle = People(p, i, l, r)
            self.middle.left = People(-1, 0, 0, l)
            self.middle.right = People(-2, i, r, 0)

            return max(self.middle.r, self.middle.l), min(self.middle.r, self.middle.l)
        else:
            # navigate
            divisor = self.get_spacy_people(self.middle)

            # add
            if divisor.r > divisor.l:
                # Add right
                i, l, r = self.get_indexes(divisor.r)
                divisor.right = People(p, i, l, r)
                divisor.r = divisor.r - 1 # space to right got smaller
                return max(divisor.right.r, divisor.right.l), min(divisor.right.r, divisor.right.l)
            else:
                # Add left
                i, l, r = self.get_indexes(divisor.l)
                divisor.left = People(p, i, l, r)
                divisor.l = divisor.l - 1 # space to left got smaller
                return max(divisor.left.r, divisor.left.l), min(divisor.left.r, divisor.left.l)


    def get_spacy_people(self, middle):
        # caso base
        if middle.left is None and middle.right is None:
            return middle

        if middle.r > middle.l:
            if middle.right is not None:
                middle.r = middle.r - 1 # One person will be added to right
                return self.get_spacy_people(middle.right) # Dive right
            else:
                return middle
        else:
            if middle.left is not None:
                middle.l = middle.l - 1 # One persion will be added to left
                return self.get_spacy_people(middle.left) # Dive left
            else:
                return middle

class People(object):
    def __init__(self, p, i, l, r):
        self.p = p
        self.i = i
        self.l = l # still empty
        self.r = r # still empty
        self.left = None
        self.right = None

def allocate_people(nstalls, npeople):
    stalls = Stalls(nstalls)

    for i in range(1, npeople+1):
        maxLR, minLR = stalls.add_people(i)

    return maxLR, minLR

def main():
    # read number of tests
    ntests = int(input())

    for t in range(0, ntests):
        # read last number counted
        nstalls, npeople = [int(s) for s in input().split(" ")]
        maxLR, minLR = allocate_people(nstalls, npeople)
        print("Case #{}: {} {}".format(t+1, maxLR, minLR))

if __name__ == '__main__':
    main()
