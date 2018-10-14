if __name__ == "__main__":
    with open('/home/roberta/Documenti/gcj/B-small0.in', 'r') as filein:
        lines = filein.readlines()
        output = open('/home/roberta/Documenti/gcj/B_small0.out', 'w')
        for p, line in enumerate(lines[1:]):
            num = [int(el) for el in line.strip()]
            i = len(num)-1
            while i>0:
                if num[i] < num[i-1]:
                    num[i-1] -= 1
                    num[i:]=[9]*len(num[i:])
                i -= 1

            res= int(''.join([str(el) for el in num]))
            output.write('Case #' + str(p + 1) + ': ' + str(res) + '\n')