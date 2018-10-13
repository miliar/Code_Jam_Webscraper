INPUT = {
    'dirs': ('string', 'multiarray')
    
}

TEST = ('''\
3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b
''','''\
Case #1: 4
Case #2: 0
Case #3: 4
''')


def count_mkdirs(dir, existing, mkdir):
    if dir == '': return mkdir
    try:
        existing.index(dir)
        return mkdir
    except:
        # directory does not exist
        existing.append(dir)
        return count_mkdirs(dir.rpartition('/')[0], existing, mkdir+1)

def main(dirs):
    existing, new = dirs
    mkdir = 0
    for d in new:
        mkdir += count_mkdirs(d, existing, 0)
    return mkdir