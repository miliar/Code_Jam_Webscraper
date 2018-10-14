import unittest

def get_minimial_switches(search_engines, queries):
    """
    This function walk throughs the list of queries, and remembers which search_engines we have already seen.
    Whenever we saw all search engines, the switches count is incremented, and we start again.
    To avoid recursion etc. we use a "direction flag" to mark seen search_engines and keep a count of 
    how much search engines we already saw.  The dirty trick is using the counter increments or decreases depending
    on the flag:  this way we don't need to reset the hash after each switch!
    """
    switches = 0
    counter = len(search_engines)
    max_counter = counter-1
    direction = -1
    for query in queries:
        if search_engines[query] != direction:
            counter += direction
            if (direction == -1 and counter == 0) or (direction == 1 and counter == max_counter):
                switches +=1
                direction = -direction
            else:
                search_engines[query] = direction
                
    return switches

class TestCenteralSystem(unittest.TestCase):

    def testgetminimalswitches(self):
        self.assertEqual(get_minimial_switches({'A':1,  'B':1}, ['A',  'A', 'A',  'A', 'B',  'A', 'A',  'B']),  3)
        self.assertEqual(get_minimial_switches({'A':1,  'B':1}, ['A',  'A', 'B',  'B', 'B',  'A', 'A',  'A']),  2)
        self.assertEqual(get_minimial_switches({'A':1,  'B':1,  'C':1}, ['A',  'A', 'B',  'B', 'B',  'A', 'A',  'A']),  0)
        self.assertEqual(get_minimial_switches({'A':1,  'B':1,  'C':1}, ['C',  'A', 'B',  'B', 'B',  'A', 'A',  'C']),  2)

def main():
    """ Reads data from standard input, process, and write results to standard output """
    count = int(raw_input())
    for i in range(1,  count+1):
        search_engine_count = int(raw_input())
        search_engines = {}
        for j in range(1,  search_engine_count+1):
            search_engines[raw_input()] = 1
        query_count = int(raw_input())
        queries = []
        for j in range(1,  query_count+1):
            queries.append(raw_input())
        print  'Case #' + str(i)  + ': ' + str(get_minimial_switches(search_engines, queries))

#unittest.main()
main()
