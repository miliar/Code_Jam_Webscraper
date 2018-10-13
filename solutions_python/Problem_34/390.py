import re

class Trie:
    end_node = {}

    """
    A Trie is like a dictionary in that it maps keys to values. However,
    because of the way keys are stored, it allows look up based on the
    longest prefix that matches.
    """

    def __init__(self):
        self.root = {}

    def add(self, key):
        """
        Add the given value for the given key.
        """
        curr_node = self.root
        for ch in key:
            curr_node = curr_node.setdefault(ch, {})
        curr_node['$'] = {} 
    #
    #
    #def find(self, key):
    #    """
    #    Return the value for the given key or None if key not found.
    #    """
    #    
    #    curr_node = self.root
    #    for ch in key:
    #        try:
    #            curr_node = curr_node[1][ch]
    #        except KeyError:
    #            return None
    #    return curr_node[0]
    #
    #
    #def find_prefix(self, key):
    #    """
    #    Find as much of the key as one can, by using the longest
    #    prefix that has a value. Return (value, remainder) where
    #    remainder is the rest of the given string.
    #    """
    #    
    #    curr_node = self.root
    #    remainder = key
    #    for ch in key:
    #        try:
    #            curr_node = curr_node[1][ch]
    #        except KeyError:
    #            return (curr_node[0], remainder)
    #        remainder = remainder[1:]
    #    return (curr_node[0], remainder)
    #
    #
    #def convert(self, keystring):
    #    """
    #    convert the given string using successive prefix look-ups.
    #    """
    #    
    #    valuestring = ""
    #    key = keystring
    #    while key:
    #        value, key = self.find_prefix(key)
    #        if not value:
    #            return (valuestring, key)
    #        valuestring += value
    #    return (valuestring, key)
    #    
        
                
def test_case_recursive(terminals_fixed, index, trie_node):
    if len(terminals_fixed) == index:
        return 1
    count = 0
    for letter in terminals_fixed[index]:
        if not trie_node.has_key(letter):
            continue
        count += test_case_recursive(terminals_fixed, index + 1, trie_node[letter])
    return count

def parse_str(str_to_parse):
    pattern = r"\(?([a-z]+)\(?|([a-z])"
    str_to_parse

def main():
    bla = r"D:\Project CodeJam\Test\A-large.in"
    #bla = r"D:\Project CodeJam\Test\1.txt"
    
    f = open(bla)
    lines = f.readlines()
    f.close()

    f_write = open(r"D:\Project CodeJam\Test\output3.txt", "w")
    t = Trie()

    line1 = lines[0]
    (L, D, N) = tuple(int(x) for x in line1.split(" "))
    for word_index in range(1, D + 1):
        t.add(lines[word_index])

    pattern = r"(?:\(?[a-z]+\)?)"
    
    for test_case_index in range(1, N + 1):
        test_case = lines[D + test_case_index]        
        terminals = re.findall(pattern, test_case)
        
        terminals_fixed = []
        for letters in terminals:
            if letters[0] == '(':
                terminals_fixed.append(letters[1:-1])
            else:
                for letter in letters:
                    terminals_fixed.append(letter)
        count_possible_words = test_case_recursive(terminals_fixed, 0, t.root)
        new_str = "Case #%d: %d\n" % (test_case_index, count_possible_words)
        f_write.write(new_str)
    f_write.close()
    print "Done"
    
main()