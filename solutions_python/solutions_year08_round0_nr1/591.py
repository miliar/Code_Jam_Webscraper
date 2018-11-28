#!/usr/bin/env python

import sys

class DataSet(object):
    """
    load dataset from into cases.

    #test theee data...

    >>> ds = DataSet("saving_the_universe_sample")
    >>> len(ds.cases) == 2
    True

    >>> ds.cases[0].search_engines
    ['Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol']

    >>> ds.cases[0].searches
    ['Yeehaw', 'Yeehaw', 'Googol', 'B9', 'Googol', 'NSM', 'B9', 'NSM', 'Dont Ask', 'Googol']

    >>> ds.cases[1].search_engines
    ['Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol']

    >>> ds.cases[1].searches
    ['Googol', 'Dont Ask', 'NSM', 'NSM', 'Yeehaw', 'Yeehaw', 'Googol']

    #test the results
    """

    def __init__(self, file):
        file = open(file)
        lines = file.readlines()
        file.close()

        self.cases = []

        nline=0
        nbcase = int(lines[nline].split('\n')[0])
        for ncase in range(nbcase):
            nline +=1
            nbsearch_engines = int(lines[nline].split('\n')[0])
            search_engines=[]
            for nsearch_engine in range(nbsearch_engines):
                nline +=1
                search_engines.append(lines[nline].split('\n')[0])

            nline +=1
            nbsearches = int(lines[nline].split('\n')[0])
            searches = []
            for nsearch in range(nbsearches):
                nline +=1
                searches.append(lines[nline].split('\n')[0])

            self.cases.append(Case(search_engines, searches))


    def process(self):
        """
        Process the cases and return a string of the form:

        "
        Case #1: 1
        Case #2: 0
        "

        the last number of each line beeing the minimal number of switches
        needed to process all the searches without blowing up the universe.
        """

        result = ""
        for case in range(len(self.cases)):
            result += "Case #"+str(case+1)+": " +str(len(self.cases[case].switches()))
            if case < len(self.cases)-1:
                 result += "\n"

        return result

class Case(object):
    """
    A case contain two lists, the list of search engines avaiable, and the list
    of queries we need to process.
    """
    def __init__(self, search_engines, searches):
        self.search_engines = search_engines
        self.searches = searches

    def switches(self):
        """
        return the minimal number of switches needed to process every searches
        without blowing up the universe (even a far far universe may blow up a
        bit hard for us).

        >>> ds = DataSet("saving_the_universe_sample")
        >>> len(ds.cases[0].switches())
        1
        >>> len(ds.cases[1].switches())
        0
        """

        result = []
        index, se = 0, None

        while True:
            tmp = self.farest_search_engine(index, se)
            result.append(tmp[1])
            if tmp[0] == -1:
                return result[1:]
            else:
                index = tmp[0]
                se = tmp[1]

    def farest_search_engine(self, from_index, except_engine=None):
        """
        return the search engine that won't be seared for the greatest lenght
        from from_index, excepting the optional except_engine param.

        >>> ds = DataSet("saving_the_universe_sample")
        >>> ds.cases[0].farest_search_engine(0, None)
        (8, 'Dont Ask')

        >>> ds.cases[1].farest_search_engine(0, None)
        (-1, 'B9')
        """

        result = None
        maxima = 0
        for se in self.search_engines:
            if se not in self.searches[from_index:] and se is not except_engine:
                return -1,se
            else:
                value = self.searches[from_index:].index(se)+from_index
                if value > maxima:
                    maxima = value
                    result = se

        return maxima,result

if __name__ =='__main__':
    import doctest
    doctest.testmod()

    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        file = "saving_the_universe_sample"
    ds = DataSet(file)
    print (ds.process())
