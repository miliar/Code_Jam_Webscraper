
def enum_parent_dirs(dir):
    if dir: 
        yield dir
        for d in enum_parent_dirs(dir.rpartition('/')[0]):
            yield d

def num_mkdirs(existing_dirs, new_dirs):
    dirs_set = set()
    for dir in existing_dirs:
         dirs_set.update(enum_parent_dirs(dir))
    
    new_dirs_set = set()
    for dir in new_dirs:
         new_dirs_set.update(enum_parent_dirs(dir))
         
    return len(new_dirs_set - dirs_set)


def run(f):
    case_num = int(f.readline())
    for i in xrange(case_num):
        exist_num, new_num = map(int, f.readline().split())
        exist_dirs = []
        for _ in xrange(exist_num):
            exist_dirs.append(f.readline().strip())
        new_dirs = []
        for _ in xrange(new_num):
            new_dirs.append(f.readline().strip())
            
        n = num_mkdirs(exist_dirs, new_dirs)
        print "Case #%d: %d" % (i+1, n)
            
if __name__ == '__main__':
    import sys
    run(open(sys.argv[1]))