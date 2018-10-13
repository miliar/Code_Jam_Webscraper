def printstuff(case, nvalue):
    print "Case #%d: %d" %(case + 1, nvalue)


if __name__ == "__main__":
    input_file = open("A-small-attempt0.in", "r")
    cases = int(input_file.readline())
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    
    for case in range(cases):
        name, n = input_file.readline().split()
        n = int(n)
        val = 0
        substrings = []
        start = 0
        end = len(name)
        for letter in name:
            while (end - start) >= n:
                substrings.append(name[start:end])
                end -= 1
            start += 1
            end = len(name)
        for substring in substrings:
            maxconsecutive = 0
            consecutive = 0
            for letter in substring:
                if letter in consonants:
                    consecutive += 1
                    if consecutive > maxconsecutive:
                        maxconsecutive = consecutive
                else:
                    consecutive = 0
            if maxconsecutive >= n:
                val += 1
                    
        
        printstuff(case, val)
    