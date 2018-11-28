__author__ = 'jesse.vera'

if __name__ == "__main__":
    phile = open("A-small-attempt0.in", "rw+")
    num = phile.readline().strip()

    for i in xrange(int(num)):
        guess_a = int(phile.readline().strip()) - 1
        grid_a = [phile.readline().strip() for x in xrange(4)]

        guess_b = int(phile.readline().strip()) - 1
        grid_b = [phile.readline().strip() for x in xrange(4)]

        nums_a = set(grid_a[guess_a].split(' '))
        nums_b = set(grid_b[guess_b].split(' '))

        nums = set.intersection(*[nums_a, nums_b])

        if not len(nums):
            message = "Volunteer cheated!"
        elif len(nums) == 1:
            message = list(nums)[0]
        else:
            message = "Bad magician!"

        print "Case #%s: %s" % (i+1, message)