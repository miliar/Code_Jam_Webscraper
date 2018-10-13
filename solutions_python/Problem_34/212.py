import re
import sys

class AlienMsg():
    """Breaks up an alien message into its constituent tokens."""
    # match each token - a parenthesis-surrounded group of letters, or an
    # individual letter
    RE = re.compile(r"(\([^)]+\)|[^(])")

    @staticmethod
    def get_tokens(word):
        return [x if x[0]!='(' else x[1:-1]  for x in AlienMsg.RE.findall(word)]

class PrefixDict():
    """Stores suffixes hierarchically.  Will be used to store all alien words."""
    def __init__(self):
        self.suffixes = {}

    def add_suffix(self, suffix):
        """Adds a suffix to this prefix dictionary."""
        c = suffix[0]
        rest = suffix[1:]
        try:
            subdict = self.suffixes[c]
        except KeyError:
            subdict = PrefixDict()
            self.suffixes[c] = subdict
        if len(rest) > 0:
            subdict.add_suffix(rest)

    def match_msg(self, tokens):
        """Returns the number of suffixes which match this chain of tokens."""
        if len(tokens) == 0:
            assert(len(self.suffixes) == 0) # should be at the bottom
            return 1 # match!

        t = tokens[0]
        rest = tokens[1:]
        n = 0
        for c in t:
            try:
                n += self.suffixes[c].match_msg(rest)
            except KeyError:
                pass # no matches

        return n

def main():
    lines = sys.stdin.readlines()
    params = [int(x) for x in re.findall(r'\d+', lines[0])]
    assert(len(params) == 3)
    L, D, N = params

    # strip off trailing \n's
    words = [w[:L] for w in lines[1:D+1]]
    msgs = [m[:len(m)-1] for m in lines[-N:]]

    # build the prefix dictionary
    pd = PrefixDict()
    for w in words:
        pd.add_suffix(w)

    # run each test case
    case_num = 1
    for m in msgs:
        n = pd.match_msg(AlienMsg.get_tokens(m))
        print 'Case #%u: %u' % (case_num, n)
        case_num += 1

main()
