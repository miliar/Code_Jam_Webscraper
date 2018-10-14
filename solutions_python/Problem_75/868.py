'''
Created on 7/05/2011

@author: Ed
'''
import string
def magicka(infile, outfile):
    input = open(infile, "r").readlines()
    output = open(outfile, "w")
    result = []
    for lineno in xrange(1, int(input[0])+1):
        elements = input[lineno].split(" ")
        #read in combinations
        nocombinations = int(elements[0])
        combinations = []
        for i in xrange(1, nocombinations + 1):
            combined = elements[i]
            combinations.append([combined[0], combined[1], combined[2]])
        #read in opposites
        noopposites = int(elements[nocombinations + 1])
        opposites = []
        for i in xrange(nocombinations + 2, nocombinations + 2 + noopposites):
            opposers = elements[i]
            opposites.append([opposers[0], opposers[1]])
        #add single letters to list
        spell = []
        spellstart = nocombinations + noopposites + 2
        spell.append(elements[spellstart + 1][0])
        wholespell = elements[spellstart + 1]
        for i in xrange(1,  int(elements[spellstart])):
            add = True
            currentletter = wholespell[i]
        #test if this letter and the last form a combo, if so wipe the last letter from the list and add this letter
            if len(spell) > 0: #No point looking for opposites/combos when the list is empty
                for combination in combinations:
                    if spell[-1] == combination[0] and currentletter == combination[1] or spell[-1] == combination[1] and currentletter == combination[0]:
                        spell[-1] = combination[2]
                        add = False
                        currentletter = spell[-1]
                        break
        #if letter you're adding is an opposite wipe list
                for opposite in opposites:
                    if currentletter == opposite[0]:
                        for letter in spell:
                            if letter == opposite[1]:
                                spell = []
                                add = False
                    elif currentletter == opposite[1]:
                        for letter in spell:
                            if letter == opposite[0]:
                                spell = []
                                add = False
            if add:
                spell.append(currentletter)
        result.append(string.replace("Case #" + str(lineno) + ": " + str(spell) + "\n", "'",""))
    output.writelines(result)

def main():
    magicka("B-large.in", "output.out")
if __name__ == '__main__': main()