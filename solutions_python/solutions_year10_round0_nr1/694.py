class SnapperChain(list):

    def snap(self):
        upper_bound = self._get_highest_powered()
        if upper_bound == len(self):
            upper_bound -= 1

        for i in xrange(upper_bound + 1):
            self[i] = not self[i]



    def _get_highest_powered(self):
        index = 0
        for i in xrange(len(self)):
            if not self[i]:
                if self[i-1]:
                    index = i
                break
            elif i + 1 == len(self):
                index = i + 1

        return index


    def is_lit(self):
        return self._get_highest_powered() == len(self)


if __name__ == '__main__':
    num_cases = int(raw_input())

    for i in xrange(num_cases):
        num_snappers, num_snaps = map(int, raw_input().split())

        snapperchain = SnapperChain([False] * num_snappers)
        for j in xrange(num_snaps):
            snapperchain.snap()

        if snapperchain.is_lit():
            result = "ON"
        else:
            result = "OFF"

        print "Case #{0}: {1}".format(i+1, result)

