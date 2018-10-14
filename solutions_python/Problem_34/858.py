"""Problem A"""

class Node():
    """Binary tree node"""
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
            
    def addWord(self, value):
        """Tree operation: insert"""
        # no duplicates
        if value == self.value:
            return
        if value < self.value:
            # go left
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.addWord(value)
        else:
            # go right
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.addWord(value)

    def wordExists(self, value):
        """Tree operation: BST search"""
        if self.value == value:
            return True
        elif value <= self.value and self.left is not None:
            return self.left.wordExists(value)
        elif value > self.value and self.right is not None:
            return self.right.wordExists(value)
        else:
            return False

class BinarySearchTree():
    """Binary search tree"""
    def __init__(self):
        self.root = None

    def addWord(self, value):
        if self.root is None:
            # create root node
            self.root = Node(value)
        else:
            self.root.addWord(value)

    def wordExists(self, value):
        return self.root.wordExists(value)

class MultiTree():
    """This 'MultiTree' is made up of L different BST's,
    where L is the number of letters in the word. This means
    any word can be searched for, as well as the first N letters
    of any word, in O(nlogn) time. Memory cost is multiplied
    by L. So D*L^2 is memory footprint"""
    def __init__(self, L):
        """A list of L binary trees.
        Each one contains an additional character"""
        self.L = L
        self.trees = [BinarySearchTree()]*L
    
    def addWord(self, value):
        """Add 'value' and all its substrings to respective trees"""
        # both range() AND [:] are end-exclusive
        for i in range(0, self.L):
            self.trees[i].addWord(value[:i+1])

    def wordExists(self, value):
        """See if word or substring exists in O(nlogn) time"""
        # select tree based on word length
        return self.trees[len(value)-1].wordExists(value)

class Garble(list):
    """A token list where letters are 'character' type and character
    choices are 'list' type. Extends list. Constructed from garbled
    transmission"""
    def __init__(self, rx):
        self.rx = rx
        # the tokens. character type for normal character;
        # list type for character combinations
        doingCombo = False
        combo = []
        for char in rx:
            if char == '\r' or char == '\n':
                continue
            if char == '(':
                doingCombo = True
            elif char == ')':
                doingCombo = False
                # add the combo tokens to the token list
                self.append(combo)
                combo = []
            elif doingCombo:
                combo.append(char)
            else:
                # just add letter
                self.append(char)

def test():
    bst = MultiTree(L=5)
    bst.addWord("hello")
    bst.addWord("world")
    bst.addWord("wilds")
    bst.addWord("walde")
    bst.addWord("weldf")
    print "mutlitree test"
    print bst.wordExists("hello")
    print bst.wordExists("world")
    print bst.wordExists("wilds")
    print bst.wordExists("walde")
    print bst.wordExists("wel")
    print bst.wordExists("w")
    print bst.wordExists("nope")
    print bst.wordExists("n")
    print "garble test"
    garble = Garble ("(zyx)bc")
    print garble

import types
# each combo is gonna take up L bytes (ASCII)
import copy

count = 0
def process(L, dictionary, garble, index):
    global count
    if type(garble[index]) == types.ListType:
        # combo
        # choose each combination
        for char in garble[index]:
            # create new garbles by copying
            # this one and fixing the combo
            # to a specific possibility
            newGarble = copy.copy(garble)
            newGarble[index] = char
            # selection: does a word with this substring
            # exist in dictionary? only look as far as we have processed.
            # this way, only viable possibilities are pursued
            if dictionary.wordExists(("".join(newGarble[:index+1]))):
                # are we at the end of the word?
                if index+1 == L:
                    # we found a combination
                    count += 1
                else:
                    # recurse: move to next token
                    process(L, dictionary, newGarble, index+1)
    else:
        # regular character.
        # are we at the end of the word?
        if index+1 == L:
            if dictionary.wordExists(("".join(garble))):
                count += 1
        else:
            # move to next token
            process(L, dictionary, garble, index+1)
            pass

def main():
    global count
    # INPUT
    import sys
    readParameters = False
    wordsRead = 0
    garbledMessages = []
    dictionary = None

    L = 0
    D = 0
    N = 0
    
    for line in sys.stdin.readlines():
        # parameters
        if not readParameters:
            readParameters = True
            # read parameters and cast
            (L,D,N) = [int(n) for n in line.split(" ")]
            dictionary = MultiTree(L)
        # dictionary
        elif wordsRead < D:
            dictionary.addWord(line)
            wordsRead += 1
        # garbled messages
        else:
            garbledMessages.append(Garble(line))

    # PROCESS
    for i, garble in enumerate(garbledMessages):
        count = 0
        # process each message, starting from first token
        process(L, dictionary, garble, 0)
        # OUTPUT
        print "Case #%d: %d" % (i+1, count)


if __name__ == "__main__":
    #test()
    main()