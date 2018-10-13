import time
import os


class SimonSolver:
    def __init__(self, output_file):
        self.start_time = None
        self.end_time = None
        self.data = None
        self.output_file = './output/' + output_file

        try:
            open(self.output_file)
            os.remove('./' + output_file)
        except OSError:
            # doesn't exist, don't need to clear
            pass
        except IOError:
            # doesn't exist, don't need to clear
            pass

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        print 'Took ' + str(self.end_time - self.start_time) + ' seconds to process.'

    def read_file(self, file):
        file = open(file, 'r')
        self.data = file.read()
        self.data = self.data.split('\n')
        return self.data

    def output(self, data):
        file = open(self.output_file, 'w+')
        for datum in data:
            file.write(datum + '\n')
        file.close()

    def output_with_case_numbers(self, data):
        file = open(self.output_file, 'w+')
        for i, datum in enumerate(data):
            file.write('Case #' + str(i + 1) + ': ' + datum + '\n')
        file.close()
