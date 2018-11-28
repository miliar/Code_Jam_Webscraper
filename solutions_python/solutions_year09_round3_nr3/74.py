def generate_permutations(word):
    """returns a list of permutations of the elements of the word. Is suboptimal..."""
    if len(word) == 1:
        return [word]
    perms = []
    word = [_ for _ in word]
    word.sort()
    for letter in word:
        newword = ''.join(_ for _ in word if not _ == letter)+letter*(word.count(letter)-1)
        perms += [letter + _ for _ in generate_permutations(newword)]
    return perms

cases = [_.strip("\n") for _ in open("C.in","rt").readlines()]
nums = int(cases[0])
print nums
tests = [(int(cases[num*2+1].split(" ")[0]),[int(_) for _ in cases[num*2+2].split(" ")])for num in range(nums)]
outfile = open("C.out","wt")

for test_num, test in enumerate(tests):
    cells, people = test
    #print cells
    min_bribed = cells * people * 1000
    for perm in generate_permutations("".join([chr(_) for _ in people])):
        prisoners = [1] * 110
        prisoners[0] = 0
        prisoners[cells+1] = 0
    
        perm =[ord(_) for _ in perm]
        bribed = 0
        #print perm
        for released in perm:
            prisoners[released] = 0
            x = released-1
            while prisoners[x] == 1:
                x -= 1
                bribed += 1
            x = released+1
            while prisoners[x] == 1:
                x += 1
                bribed += 1
            #print bribed
        min_bribed = min(min_bribed, bribed)
    print min_bribed
    outfile.write("Case #%d: %d\n" % (test_num+1, min_bribed))


