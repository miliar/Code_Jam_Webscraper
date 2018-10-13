

class Item(object):
    def __init__(self, index=0):
        self.index = index
        self.parents = []
        self.childs = []

    def is_source(self):
        return len(self.parents) > 1

    def is_dest(self):
        return len(self.childs) > 1

    def get_dests(self):
        if len(self.parents):
            dests = []
            for parent in self.parents:
                dests.extend(parent.get_dests())
            return dests
        else:
            return [self]



if __name__ == '__main__':
    T = int(raw_input())
    for test_index in xrange(1, T+1):
        N = int(raw_input())

        items = [Item(_) for _ in xrange(N+1)]

        for index in xrange(1, N+1):
            nums = map(int, raw_input().split())
            Mi,Ii = nums[0], nums[1:]
            for ii in Ii:
                items[index].parents.append(items[ii])
                items[ii].childs.append(items[index])

        src_items = filter(lambda item: item.is_source(), items)
        dst_items = filter(lambda item: item.is_dest(), items)

        def check_item(item):
            dests = item.get_dests()
            for dest in set(dests):
                if dests.count(dest) > 1:
                    return True
            return False

        result = False

        for src_item in src_items:
            if check_item(src_item):
                result = True
                break

        print 'Case #%d: %s' % (test_index, 'Yes' if result else 'No')
