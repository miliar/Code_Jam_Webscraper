class OutputWriter:

    def print(self, cases, filepath):
        with open(filepath, 'w') as f:
            for i in range(len(cases)):
                f.write('Case #' + str(i+1) + ': ' + cases[i] + '\n')