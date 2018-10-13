'''
Created on 13 Apr 2012

@author: Mike
'''
class GoogleCodeJamInput(object):
    def __init__(self, input_file):
        self.parsed_input = None
        
        with open(input_file, 'r') as f:
            self.input = f.read()
            
        self._parse_input()
    
    def _parse_input(self):
        self.parsed_input = self.input.splitlines()[1:]
    
    def get_parsed_input(self):
        return self.parsed_input
    
class GoogleCodeJamOutput(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.output_data = None
        
    def process_input(self):
        raise NotImplementedError
            
    def print_output(self):
        print self.output_data
        
    def write_output(self):
        with open('outputfiles/%s.out' % self.__class__.__name__, 'w') as f:
            f.write(self.output_data)
    
class SpeakingInTongues(GoogleCodeJamOutput):
    
    LETTER_MAPPINGS = {'y': 'a',
                       'n': 'b',
                       'f': 'c',
                       'i': 'd',
                       'c': 'e',
                       'w': 'f',
                       'l': 'g',
                       'b': 'h',
                       'k': 'i',
                       'u': 'j',
                       'o': 'k',
                       'm': 'l',
                       'x': 'm',
                       's': 'n',
                       'e': 'o',
                       'v': 'p',
                       'z': 'q',
                       'p': 'r',
                       'd': 's',
                       'r': 't',
                       'j': 'u',
                       'g': 'v',
                       't': 'w',
                       'h': 'x',
                       'a': 'y',
                       'q': 'z',
                       ' ': ' '}
        
    def process_input(self):
        self.output_data = ''
        for index, line in enumerate(self.input_data):
            self.output_data += 'Case #%i: ' % (index+1)
            for letter in line:
                self.output_data += self.LETTER_MAPPINGS[letter]
            if (index < len(self.input_data) - 1):
                self.output_data += '\n'
    
if __name__ == "__main__":
    import os
    input = GoogleCodeJamInput(os.path.join('inputfiles', os.listdir('inputfiles')[0]))
    parsed_input = input.get_parsed_input()
    tongues = SpeakingInTongues(parsed_input)
    tongues.process_input()
    tongues.print_output()
    tongues.write_output()
        