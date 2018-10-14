import sys
import os


def main():
	s = ''.join(sys.stdin.readlines()).split()
	os.close(0)

        L = int(s[0])
        D = int(s[1])
        N = int(s[2])

        s = s[3:]

        dict = set([])
        
        for i in range(D):
            dict.add(s[0])
            s = s[1:]


        sets = []
        for i in range(L):
            sets += [set([])]

        for i in dict:
            for j in range(1,L+1):
                sets[j-1].add(i[0:j])


        case = 0
        while case < N:
            word = s[case]
            letters = []
            for i in range(L):
                letters += [[]]
                if word[0] == "(":
                    firstEnd =  word.find(")")
                    for letter in word[1:firstEnd]:
                        letters[i] += [letter]
                    word = word[firstEnd+1:]
                else:
                    letters[i] += [word[0]]
                    word = word[1:]

            matches = findMatches(sets, letters, L, D, N)
                
            print "Case #" + str((case+1)) + ": " + str(matches)

            case += 1

def findMatches(sets, letters, L, D, N):
    matches = 1
    sets = [1] + sets
    newLets = reduce(lambda x, y: dropAndCombine(sets, x, y), letters)
    return len([item for item in newLets if item in sets[len(sets)-1]])

def dropAndCombine(sets, letters0, letters1):
    letters0 = [item for item in letters0 if item in sets[sets[0]]]
    sets[0]+=1
    
    if len(letters0) == 0:
        return []
    newLet0 = []
    for i in letters0:
        combLet0 = map(lambda X: i+X, letters1)
        newLet0 += combLet0
    return newLet0

if __name__ == "__main__":
 	main()

