
class PancakeFlipper:
    def __init__(self, S, K):
        """
        pancacke flippers with a row of pancakes S and a flipper of length K
        :param S:
            String, composed of +(head)/-(tail)
        :param K:
            Length of flipper (>= S)
        """
        assert all(x in ('+', '-') for x in S)
        assert 2 <= K <= len(S)
        self.S = list(x=='+' for x in S)
        self.K = K
        self.n_flips = 0

    def __str__(self):
        print(['+' if x else '-' for x in self.S])

    def flip(self, i):
        """
        flip
        :param i: int, offset
        :return: None
        """
        self.S[i:i+self.K] = [not x for x in self.S[i:i+self.K]]
        self.n_flips += 1

    def flip_all_head(self):
        """
        flip all pancakes to head
        :return: String: # of required flips or
                 "IMPOSSIBLE" if the task is impossible.
        """
        for i in range(len(self.S)-self.K+1):
            if not self.S[i]:
                self.flip(i)

        if all(self.S[len(self.S)-self.K+1:]):
            return self.n_flips
        else:
            return 'IMPOSSIBLE'

if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        S, K = input().split(" ")  # read a list of integers, 2 in this case
        pf = PancakeFlipper(S, int(K))
        output = pf.flip_all_head()
        print("Case #{}: {}".format(i, output))