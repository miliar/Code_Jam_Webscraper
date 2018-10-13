
def LoadInput():

   with open("input.txt") as f:
      return f.read()
   
def Output(text):

   with open("output.txt", "w") as f:
      f.write(text)

def ParseInput(text):

    text = text.split('\n')

    lines = int(text.pop(0))
    return [ map(int, line.split()) for line in text[:lines] ]

def DoTestCase(case):
    
    N, K = case

    chain = ''.join(reversed(bin(K)))

    if chain.startswith('1' * N):
        return 'ON'
    return 'OFF'
    

def main():

    testCases = ParseInput(LoadInput())

    result = []
    
    for i, case in enumerate(testCases):
        result.append("Case #{0}: {1}".format(i + 1, DoTestCase(case)))

    result = '\n'.join(result)

    Output(result)
    print "done, result:"
    print result


    

if __name__ == "__main__":

    main()
