class Panckakes:
    def __init__(self, s, k):
        self.s = s
        self.k = k

    def get_min_flips(self):
        count = 0
        while self.s.count("-") > 0:
            pos = self.get_pos_of_blank()
            if pos == -1:
                return count
            if pos > (len(self.s) - k):
                return "IMPOSSIBLE"
            self.flip(pos)
            count += 1
        
        return count

    def flip(self, start):
        for i in range(start, start + self.k):
            if s[i] == "-":
                s[i] = "+"
            else:
                s[i] = "-"

    def get_pos_of_blank(self):
        temp = ''.join(self.s)
        return temp.find("-")

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        s, k = [j for j in input().split(" ")]
        s = [ch for ch in s]
        k = int(k)
        pancakes = Panckakes(s,k)
        flips = pancakes.get_min_flips()
        print("Case #{}: {}".format(i, flips))