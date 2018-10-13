import sys
class PancakeFlipper:
    def __init__(self, num, k):
        sys.stderr.write("creating pf " + str(num) + " " + str(k) + "\n")
        self.pancakes = num
        self.k = int(k)
    def areAllUp(self, l):
        length = len(l)
        correct = ["+"] * length
        return l == correct
    def getFlipCount(self):
        flips = 0
        self.pancakes = list(self.pancakes)
        interations = len(self.pancakes) - self.k + 1
        for x in range(interations):
            if self.pancakes[x] == "-":
                flips += 1
                for j in range(x, x+self.k):
                    flip = "+" if self.pancakes[j] == '-' else "-"
                    self.pancakes[j] = flip
        arePAllUp = self.areAllUp(self.pancakes)
        if arePAllUp:
            return str(flips)
        else:
            return "IMPOSSIBLE"
num_of_cases = int(input())
results = {}
for x in xrange(num_of_cases):
    sys.stderr.write("on case " + str(x) + "\n")
    pancake_in = raw_input().split(" ")
    pancake_list = pancake_in[0]
    k = pancake_in[1]
    flipper = PancakeFlipper(pancake_list, k)
    result = flipper.getFlipCount()
    results[x+1] = result
for key, res in results.items():
    print("Case #" + str(key) + ": " + str(res))
