"""
The first line of the input gives the number of test cases, T. T  test cases follow.
Each case begins with a line containing two integers N and M, separated by a space.

The next N lines each give the path of one directory that already exists on your
computer. This list will include every directory already on your computer other than
the root directory. (The root directory is on every computer, so there is no need to
list it explicitly.)

The next M lines each give the path of one directory that you want to create.

Each of the paths in the input is formatted as in the problem statement above.
Specifically, a path consists of one or more lower-case alpha-numeric strings (i.e.,
strings containing only the symbols 'a'-'z' and '0'-'9'), each preceded by a single
forward slash. These alpha-numeric strings are never empty.
-------------------
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
-------------------
Case #2: [['home', 'gcj', 'finals'], ['home', 'gcj', 'quals']]
Case #1: [['chicken']]
Case #3: [['a', 'b'], ['a', 'c'], ['b', 'b']]
-------------------
Case #1: {'home': {'gcj': {'quals': {}, 'finals': {}}}}
Case #2: {'chicken': {}}
Case #3: {'a': {'c': {}, 'b': {}}, 'b': {'b': {}}}
-------------------
Case #1: 4
Case #2: 0
Case #3: 4
-------------------
To create a directory, you can use the mkdir command. You specify a path, and then
mkdir will create the directory described by that path, but only if the parent
directory already exists. For example, if you wanted to create the "/home/gcj/finals"
and "/home/gcj/quals" directories from scratch, you would need four commands:

mkdir /home
mkdir /home/gcj
mkdir /home/gcj/finals
mkdir /home/gcj/quals

Given the full set of directories already existing on your computer, and a set of new
directories you want to create if they do not already exist, how many mkdir commands
do you need to use?
"""

from sys import stdin
import psyco; psyco.full()

created = 0 # this is not nice

def add_path(tree, path):
    global created

    if path:
        root = path[0]
        others = path[1:]

        if root in tree:
            add_path(tree[root], others)
        else:
            created += 1
            tree[root] = {}
            add_path(tree[root], others)


def main():
    global created # this is not nice

    T = int(stdin.readline())
    for tcase in xrange(T):
        tree = {}
        N, M = map(int, stdin.readline().split())

        existing = [stdin.readline().strip().split("/")[1:] for i in xrange(N)]
        for path in existing:
            add_path(tree, path)

        created = 0
        tocreate = [stdin.readline().strip().split("/")[1:] for i in xrange(M)]
        for path in tocreate:
            add_path(tree, path)

        result = created
        print ("Case #%d:" % (tcase+1)), result

main()