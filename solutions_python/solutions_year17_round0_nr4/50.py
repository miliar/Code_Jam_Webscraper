from collections import defaultdict, namedtuple
import sys

Model = namedtuple('Model', 'kind row col')

class RowSet(object):
    """Gets a conversion of (row, col) -> (class, pos).
    For example, class=row, pos=col.
    Holds for each "class" all the "positions" of cells that can be used in it.
    This excludes the classes and positions that are already occupied.
    """

    def __init__(self, conv, convback):
        self._classes = defaultdict(set)
        self._occupied_classes = set()
        self._occupied_positions = set()
        self.conv = conv
        self.convback = convback

    def mark_occupied(self, row, col):
        cls, pos = self.conv(row, col)
        self._occupied_classes.add(cls)
        self._occupied_positions.add(pos)

    def add_cell(self, row, col):
        cls, pos = self.conv(row, col)
        if cls not in self._occupied_classes and pos not in self._occupied_positions:
            self._classes[cls].add(pos)

    def get_addable_cells(self):
        classes = sorted(self._classes.items(),
                         key=lambda (cls, poses): len(poses))
        for i in range(1, len(classes)):
            assert classes[i-1][1] <= classes[i][1]
        addable_cells = []
        used_poses = set()
        for cls, poses in classes:
#            free_poses = poses - used_poses
#            if free_poses:
#                pos = next(iter(free_poses))
#                used_poses.add(pos)
#                addable_cells.append(self.convback(cls, pos))
            for pos in sorted(poses):
                if pos not in used_poses:
                    used_poses.add(pos)
                    addable_cells.append(self.convback(cls, pos))
                    break
        return addable_cells


class Board(object):
    def __init__(self):
        self._board = {}

    def get(self, row, col):
        key = (row, col)
        return self._board.get(key)

    def set(self, row, col, kind):
        key = (row, col)
        curr = self._board.get(key)
        if curr is None or curr == kind:
            self._board[key] = kind
        else:
            self._board[key] = 'o'

    def bulk_set(self, cells, kind):
        for (row, col) in cells:
            self.set(row, col, kind)

    def get_score(self):
        score = 0
        for val in self._board.itervalues():
            score += 2 if val=='o' else 1
        return score

    def get_models_minus(self, other):
        return [Model(kind=k, row=r, col=c)
                for (r,c), k in self._board.iteritems()
                if other.get(r, c) != k]

    def pprint(self, N):
        print ''
        for row in range(1, N+1):
            vals = [self._board.get((row, col), '.') for col in range(1, N+1)]
            print ''.join(vals)
        print ''


def add_best(N, initial):
    """returns (points, added-models)."""
    board = Board()
    initial_board = Board()
    iden = lambda x, y: (x, y)
    orthoset = RowSet(iden, iden)
    diagsets = [RowSet(lambda row, col: (row+col, row-col),
                       lambda cls, pos: ((cls+pos)/2, (cls-pos)/2))
                for _ in range(2)]

    for model in initial:
        r, c = model.row, model.col
        board.set(r, c, model.kind)
        initial_board.set(r, c, model.kind)
        if model.kind != '+':
            orthoset.mark_occupied(r, c)
        if model.kind != 'x':
            diagsets[(r+c)%2].mark_occupied(r, c)

    for r in range(1, N+1):
        for c in range(1, N+1):
            orthoset.add_cell(r, c)
            diagsets[(r+c)%2].add_cell(r, c)

    board.bulk_set(orthoset.get_addable_cells(), 'x')
    board.bulk_set(diagsets[0].get_addable_cells(), '+')
    board.bulk_set(diagsets[1].get_addable_cells(), '+')
    final_score = board.get_score()
    added_models = board.get_models_minus(initial_board)
    # board.pprint(N)  # for checking
    return final_score, added_models


if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N, M = [int(part) for part in sys.stdin.readline().split()]
        initial = []
        for _ in range(M):
            kind, r, c = sys.stdin.readline().split()
            assert kind in ['+', 'x', 'o']
            initial.append(Model(kind, int(r), int(c)))
        points, added_models = add_best(N, initial)
        print "Case #%d: %d %d" % (i+1, points, len(added_models))
        for model in added_models:
            print "%s %d %d" % (model.kind, model.row, model.col)
