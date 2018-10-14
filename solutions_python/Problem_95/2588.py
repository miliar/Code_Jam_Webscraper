googlerese_example = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
googlerese_example = [c for c in googlerese_example]

translation_example = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
translation_example = [c for c in translation_example]

dictionary = dict([(googlerese_example[i],translation_example[i]) for i in range(len(googlerese_example))])
dictionary['q'] = 'z'
dictionary['z'] = 'q'

def solve(file_path):
    file_in = file(file_path, 'r')
    file_out = file('A-small.out', 'w')

    i = 0
    ammount_of_cases = 0
    case_number = 0

    for line in file_in:
        if i == 0:
            ammount_of_cases = int(line)
            i = 1
        elif i == 1:
            case_number = case_number + 1
            if case_number == ammount_of_cases:
                if line[:-1] <> '':
                    file_out.write('Case #' + str(case_number) + ': ' + translate(line))
            else:
                file_out.write('Case #' + str(case_number) + ': ' + translate(line[:-1]) + '\n')

    file_in.close()
    file_out.close()
            

def translate(googlerese):
    translation = ''.join([dictionary[key] for key in googlerese if key <> '\n'])
    return translation
