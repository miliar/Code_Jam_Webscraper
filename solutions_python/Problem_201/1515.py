class LinkedList(object):
    def __init__(self):
        self.head = None

    def ordered_insert(self, distance):
        if self.head is None:
            self.head = LinkedNode(distance)
            return
        if self.head.distance < distance:
            new_node = LinkedNode(distance)
            new_node.next = self.head
            self.head = new_node
            return
        elif self.head.distance == distance:
            self.head.count += 1
            return
        current_node = self.head.next
        previous_node = self.head
        while current_node is not None:
            if current_node.distance == distance:
                current_node.count += 1
                return
            if current_node.distance < distance:
                new_node = LinkedNode(distance)
                new_node.next = current_node
                previous_node.next = new_node
                return
            previous_node = current_node
            current_node = current_node.next
        new_node = LinkedNode(distance)
        previous_node.next = new_node

    def pop(self):
        next_node = self.head.next
        self.head = next_node

    # def get_head(self):
    #     return self.head.distance

class LinkedNode(object):
    def __init__(self, distance):
        self.next = None
        self.distance = distance
        self.count = 1


def solution(stalls, persons):
    intervals = LinkedList()
    intervals.ordered_insert(stalls)
    for person in xrange(0, persons):
        top = intervals.head
        left = top.distance / 2
        right = left
        if top.distance % 2 == 0:
            left -= 1
        top.count -= 1
        if not top.count:
            intervals.pop()
        intervals.ordered_insert(left)
        intervals.ordered_insert(right)

    return max(left, right), min(left, right)


files = [
    # 'test.in',
    'C-small-2-attempt1.in',
]

if __name__ == '__main__':
    for filename in files:
        outfilename = filename.replace('.in', '.out')
        with open(filename, 'r') as f:
            with open(outfilename, 'w') as w:
                no_lines = int(f.readline())
                results = []
                for index in xrange(0, no_lines):
                    input_data = f.readline()
                    N, K = input_data.split(' ')
                    print 'Processing case {}'.format(index + 1)
                    result = solution(int(N), int(K))
                    w.writelines("Case #{}: {} {}\n".format(index + 1, *result))
