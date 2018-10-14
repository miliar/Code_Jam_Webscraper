def file2stringlist(filepath, stringlist):
    file = open(filepath, 'r')
    for line in file:
        stringlist.append(line)
        pass
    file.close()
    del file
    pass

def stringlist2file(stringlist, filepath):
    file = open(filepath, 'w')
    for string in stringlist:
        file.write(string)
        pass
    file.close()
    del file
    pass

def solution(inputpath, outputpath, processor):
    inputstrings = list()
    file2stringlist(inputpath, inputstrings)
    outputstrings = list()
    processor.process(inputstrings, outputstrings)
    del inputstrings
    stringlist2file(outputstrings, outputpath)
    del outputstrings
    pass

class Problem:
    pass

class Output:
    pass

def process(
    inputstrings,
    outputstrings,
    problem_separator,
    problem_composer,
    algortihm,
    output_formatter
):
    """problem_separator has separate(fulltext, problemtexts)
    problem_composer has compose(problemtext, problemobject)
    algorithm has run(problemobject, outputobject)
    output_formatter has formato(outputobject, outputtext)"""
    problemtexts = list()
    problem_separator.separate(inputstrings, problemtexts)
    for problemtext in problemtexts:
        problemobject = Problem()
        problem_composer.compose(problemtext, problemobject)
        outputobject = Output()
        algortihm.run(problemobject, outputobject)
        del problemobject
        outputtext = list()
        output_formatter.formato(outputobject, outputtext)
        del outputobject
        for line in outputtext:
            outputstrings.append(line)
            pass
        del outputtext
        pass
    del problemtexts
    pass

class Processor:
    def process(self, inputstrings, outputstrings):
        process(
            inputstrings,
            outputstrings,
            self.problem_separator,
            self.problem_composer,
            self.algorithm,
            self.output_formatter
        )
        pass

    pass
