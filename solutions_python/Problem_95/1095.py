import collections
import pprint
import sys
import itertools
import math

f = "A-small-attempt2.in"
lines = open(f).readlines()
lines = [line.strip() for line in lines]
input_length = int(lines.pop(0))
lines = lines[:input_length]
#print lines


mapping = {
'y':'a',
'e':'o',
'q':'z',
# Depending on wording of question might not be known for real problem
' ':' ',
# Could use the rest of the mapping from the sample, but that would be too easy!
# Too easy sounds good after several hours:
'a':'y',
'b':'h',
'c':'e',
'c':'e',
'd':'s',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'z':'q',
}


words = open('/usr/share/dict/words').readlines()
words = [word.strip().lower() for word in words]
words = set(words)

def char_counts(chars):
    counter = collections.Counter()
    counter.update([c for c in chars])
    return counter

def reference_char_counts(words):
    counter = char_counts("".join(list(words)))
    # Approximate estimate for spaces. http://answers.yahoo.com/question/index?qid=20080526032554AAB28AF has the average word length at 5.1 characters, use this stati if the following isn't useful.
    #n = len(words)
    #counter[' ']=n
    counter[' ']=(1/5.1)*len(words)
    return counter
    
def substitute(c,mapping):
    return mapping.get(c,'-')

def substitute_string(s,mapping):
    return "".join([substitute(c,mapping) for c in s])


def guess_map(reference_in,problem_in,known):
    map = dict(known)
    reference = collections.Counter(reference_in)
    problem = collections.Counter(problem_in)
    #print reference,problem
    for (c1,c2) in map.items():
        if problem[c1]:
            problem.pop(c1)
        if reference[c2]:
            reference.pop(c2)
    for ((c1,count1),(c2,count2)) in zip(problem.most_common(),reference.most_common()):
       map[c1]=c2 
    return map
        
reference_counts = reference_char_counts(words)
problem_counts = char_counts("".join(lines))
#pprint.pprint(reference_counts)
#pprint.pprint(problem_counts)

encoding_mapping=dict([[v,k] for (k,v) in mapping.items()])
corpus = encoding_mapping[' '].join(lines)
problem_words = corpus.split(encoding_mapping[' '])

#guessed=guess_map(reference_counts,problem_counts,mapping)

#pprint.pprint(guessed)
#for line in lines[1:]:
#    print "".join([substitute(c,guessed) for c in line])
    


def is_valid(string,mapping,words=words):
    new_seq=[]
    for c in string:
        if not c in mapping:
            return False
        else:
            new_seq.append(mapping[c])
    word = "".join(new_seq)
    return word in words


words_and_length = [(len(word),word) for word in words]
words_and_length.sort()
words_and_length_groups = itertools.groupby(words_and_length,lambda x: x[0])
length_to_words = {}
for l,vals in words_and_length_groups:
    length_to_words[l] = [x[1] for x in vals]


def is_valid_partial(string,mapping):
    # Simple test implementation (terrible performance)
    chars = [mapping.get(c,None) for c in string]
    for word in length_to_words[len(chars)]:
        match=True
        for (c,c1) in zip(chars,word):
            if c and not c==c1:
                match=False
        if match:
            return True
    return False
                

def total_failures(test_words,mapping):
    return len(filter(lambda x: not x,[is_valid_partial(w,mapping) for w in test_words]))
    
    
# Best frequency matches first (roughly)
def potential_chars(c,mapping):
    if c in mapping:
        chars=[mapping[c]]
    else:
        candidates  = set(reference_counts.keys()) - set(mapping.values())
        reference_descending = [x[0] for x in reference_counts.most_common()]
        problem_descending = [x[0] for x in problem_counts.most_common()]
        pos_frac = problem_descending.index(c)/float(len(problem_descending))
        index = int(math.floor(pos_frac*len(reference_descending)))
        chars = []
        while reference_descending:
            char=reference_descending.pop(index)
            if char in candidates:
                chars.append(char)
            if index==len(reference_descending) or (index>0 and len(reference_descending)%2):
                index -=1

        chars = [c1 for c1 in candidates]
        # Decresing order
        chars.sort(cmp=lambda x,y: cmp(reference_counts[y],reference_counts[x]))
        
    return chars

# Generator for potential mappings
# Take mapping and string
# for potential substitues for char: for each potential mapping for the substring: yield new mapping containing potential substitute for char
def potential_mappings(string,mapping):
    if not string:
        yield mapping
    else:
        c = string[0]
        for c1 in potential_chars(c,mapping):
            mapping1=dict(mapping)
            mapping1.update({c:c1})
            for mapping2 in potential_mappings(string[1:],mapping1):
                result = dict(mapping2)
                result.update(mapping1)
                yield result
        
# <function 1: words>
# Start by ordering words by size
# Loop until success or max_failures = number of words (will never reach this point in a userful time period for any reasonable input)
# Set max_failures to zero
# Call function 2
# <function 2: words, mapping, failues, max_failues>
# Return false if failures =  max_failues
# Return mapping if no remaining words
# Loop over potential mappings of the current word (check by dict)
# For each valid mapping recurse with hypothethical mapping and current word removed - return mapping if success
# If no potential mappings found then recurse with incremented max failues and current word removed - return mapping if success, return false if fail

def solve(words):
    words = sorted(words,cmp=lambda x,y: cmp(len(x),len(y)))#[:17]
    def inner(words, max_failures, mapping=mapping, failures=0):
        #print words, max_failures, mapping, failures
        if failures > max_failures:
            return False
        if not words:
            return mapping
        word = words[0]
        for mapping1 in potential_mappings(word,mapping):
           if is_valid(word,mapping1):
                #print "Valid mapping"
                #print "Decoded: ",substitute_string(word,mapping1)
                #tf = total_failures(words,mapping1)
                #tf = total_failures(words,mapping1)
                tf = 0
                #print "Failures: ", failures
                #print "Total failures: ", tf
                if tf + failures <= max_failures:
                    #print "Recursing optimistically"
                    result = inner(words[1:],max_failures,mapping1,failures)
                    if result:
                        return result
                    #print "Optimistic recursion failed"
        # If we reach this point then there is no mapping for the current word that succeeded for the remainder of the input
        return inner(words[1:],max_failures,mapping,failures+1)
    for max_failures in range(len(words)):
    #for max_failures in range(2):
        result = inner(words,max_failures)
        if result:
            #print "max_failures: ",max_failures
            #print result
            return result
        #print "Failed",words
        return mapping
    return False


sorted_problem_words = sorted(problem_words,cmp=lambda x,y: cmp(len(x),len(y)))
#print sorted_problem_words

#solution_map = solve(problem_words)
#if not solution_map:
#    print "Failed"
#    sys.exit()
#pprint.pprint(solution_map)


#for word in sorted_problem_words:
#    print "".join([substitute(c,solution_map) for c in word])

for i in range(len(lines)):
    # Performance is poor with large lines, and we all a-z characters so hopefully won't run into ambiguities requiring dealing with multiple lines
    line_words = lines[i].split(encoding_mapping[" "])
    solution_map = solve(line_words)
    print "Case #%i: %s" % (i+1,"".join([substitute(c,solution_map) for c in lines[i]]))
