class OutputWriter:

    def print(self, cases, filepath):
        with open(filepath, 'w') as f:
            for i in range(len(cases)):
                count = ''

                if cases[i] == -1:
                    count = 'IMPOSSIBLE'
                else:
                    count = str(cases[i])
                f.write('Case #' + str(i+1) + ': ' + count + '\n')