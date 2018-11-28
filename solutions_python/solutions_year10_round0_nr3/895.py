import os

class QuestionC(object):

    def __init__(self):
        self.income = 0
        self.case = 1

    def start(self, filename):
        with open(filename, "a") as o:
            for i in range(self.R):
                self.board()
            o.write("Case #%d: %d\n" % (self.case, self.income))
            self.case += 1
            self.income = 0
        
    def board(self):
        """
        Remove the first x elements from queue whose sum is <=k
        Put them to the board
        Reappend them to the queue
        """
        # 1,4,2,1
        candidates = []
        total = 0

        while self.queue and total + self.queue[0] <= self.k:
            group = self.queue.pop(0)
            total += group
            candidates.append(group)

        self.on_board = candidates
        self.queue.extend(candidates)
        self.income += sum(self.on_board)


    def read(self, filename):
        """
        The first line of the input gives the number of test cases, T.
        T test cases follow, with each test case consisting of two lines.
        The first line contains three space-separated integers: R, k and N.
        The second line contains N space-separated integers gi,
        each of which is the size of a group that wants to ride.
        g0 is the size of the first group, g1 is the size of the second group, etc.

        3
        4 6 4
        1 4 2 1
        100 10 1
        1
        5 5 10
        2 4 2 3 4 2 1 2 1 3
        """
        try:
            os.remove(self.output)
        except:
            pass
        with open(filename) as f:
            num_test_cases = int(f.readline().strip())
            for case in range(num_test_cases):
                self.R, self.k, self.N = map(int, f.readline().strip().split())
                self.queue = map(int, f.readline().strip().split())
                assert self.N == len(self.queue)
                self.start(self.output)

if __name__ == "__main__":
    qc = QuestionC()
    base = "/home/emre/Download/"
    qc.output = base+"output.txt"
    qc.read(base+"C-small-attempt0.in")