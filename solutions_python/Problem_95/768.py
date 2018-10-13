from os import path, linesep
import itertools
import string

def start_translation(untranslated, output):
    """
    Solves one case of this CodeJam task and returns its solution.
    """
    for line in untranslated:
        print(line)
    print()    
    
    # translate
    translationMap = {
        " ": " ",
        "a": "y",
        "b": "h",
        "c": "e",
        "d": "s",
        "e": "o",
        "f": "c",
        "g": "v",
        "h": "x",
        "i": "d",
        "j": "u",
        "k": "i",
        "l": "g",
        "m": "l",
        "n": "b",
        "o": "k",
        "p": "r",
        "q": "z",
        "r": "t",
        "s": "n",
        "t": "w",
        "u": "j",
        "v": "p",
        "w": "f",
        "x": "m",
        "y": "a",
        "z": "q",
    }
    translatedText = translate(untranslated, translationMap)
    for i in range(0, len(translatedText)):
        translatedLine = translatedText[i]
        output.write("Case #" + str(i+1) + ": " + translatedLine + "\n")

def translate(untranslated, translationMap):
    """
    Perform a translation of the given untranslated lines based on the translations dictionary.
    """
    result = []
    for message in untranslated:
        translatedMessage = ""
        for i in range(len(message)):
            if message[i] in translationMap:
                translatedMessage += translationMap[message[i]]
            else:
                translatedMessage += "?"
        result.append(translatedMessage)
    return result


# From here on, the fairly generic CodeJam code follows. Read in file, output solutions.
# Potentially the first line does not include number of cases, this may have to be adapted.

def run_codejam():
    """
    Runs the codejam by initializing input and output, calling methods which solve the cases and finally
    outputting the results.
    """
    testfile = "A-small-attempt1"
    cases_file = path.join(path.dirname(__file__), testfile)
    with open(cases_file + ".in", "r") as cj_input:
        with open(cases_file + ".out", "w") as cj_output:
            # get a line-based reader
            reader = iter(cj_input.read().splitlines())
            
            # read number of cases
            caseCount = int(next(reader))
            
            # handle cases (1-based)
            untranslated = list(reader)
            start_translation(untranslated, cj_output)
        
# run the CodeJam analysis
run_codejam()