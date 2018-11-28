import fileinput

mult = {
    '1':  { '1': '1',  'i': 'i',  'j': 'j',  'k': 'k',  '-1': '-1', '-i': '-i', '-j': '-j', '-k': '-k' },
    '-1': { '1': '-1', 'i': '-i', 'j': '-j', 'k': '-k', '-1': '1',  '-i': 'i',  '-j': 'j',  '-k': 'k'  },
    'i':  { '1': 'i',  'i': '-1', 'j': 'k',  'k': '-j', '-1': '-i', '-i': '1',  '-j': '-k', '-k': 'j'  },
    '-i': { '1': '-i', 'i': '1',  'j': '-k', 'k': 'j',  '-1': 'i',  '-i': '-1', '-j': 'k',  '-k': '-j' },
    'j':  { '1': 'j',  'i': '-k', 'j': '-1', 'k': 'i',  '-1': '-j', '-i': 'k',  '-j': '1',  '-k': '-i' },
    '-j': { '1': '-j', 'i': 'k',  'j': '1',  'k': '-i', '-1': 'j',  '-i': '-k', '-j': '-1', '-k': 'i'  },
    'k':  { '1': 'k',  'i': 'j',  'j': '-i', 'k': '-1', '-1': '-k', '-i': '-j', '-j': 'i',  '-k': '1'  },
    '-k': { '1': '-k', 'i': '-j', 'j': 'i',  'k': '1',  '-1': 'k',  '-i': 'j',  '-j': '-i', '-k': '-1' }
}

div = {
    '1':  { '1': '1',  'i': '-i', 'j': '-j', 'k': '-k', '-1': '-1', '-i': 'i',  '-j': 'j',  '-k': 'k'  },
    '-1': { '1': '-1', 'i': 'i',  'j': 'j',  'k': 'k',  '-1': '1',  '-i': '-i', '-j': '-j', '-k': '-k' },
    'i':  { '1': 'i',  'i': '1',  'j': 'k',  'k': '-j', '-1': '-i', '-i': '-1', '-j': '-k', '-k': 'j'  },
    '-i': { '1': '-i', 'i': '-1', 'j': '-k', 'k': 'j',  '-1': 'i',  '-i': '1',  '-j': 'k',  '-k': '-j' },
    'j':  { '1': 'j',  'i': '-k', 'j': '1',  'k': 'i',  '-1': '-j', '-i': 'k',  '-j': '-1', '-k': '-i' },
    '-j': { '1': '-j', 'i': 'k',  'j': '-1', 'k': '-i', '-1': 'j',  '-i': '-k', '-j': '1',  '-k': 'i'  },
    'k':  { '1': 'k',  'i': 'j',  'j': '-i', 'k': '1',  '-1': '-k', '-i': '-j', '-j': 'i',  '-k': '-1' },
    '-k': { '1': '-k', 'i': '-j', 'j': 'i',  'k': '-1', '-1': 'k',  '-i': 'j',  '-j': '-i', '-k': '1'  }
}

dp = []

def multiply(a, b):
    return mult[a][b]

def divide(a, b):
    return div[a][b]

def scan_k(start):
    rest = divide(dp[len(dp) - 1], dp[start])
    return True if rest == "k" else False

def scan_j(start):
    for i in xrange(start, len(letters)):
        if (divide(dp[i], dp[start]) == "j"):
            if (scan_k(i)):
                return True
    return False

def scan_i():
    for i in range(len(dp)):
        if (dp[i] == "i"):
            if (scan_j(i)):
                return True
    return False

def compute(letters):
    dp.append(letters[0])
    for i in xrange(1, len(letters)):
        dp.append(multiply(dp[i-1], letters[i]))
    return scan_i()

input = fileinput.input()

cases = int(input.readline())
for c in range(cases):
    dp = []
    line = input.readline().split()
    length = int(line[0])
    reps = int(line[1])
    letters = input.readline().strip()
    letters = letters * reps

    res = "YES" if compute(letters) else "NO"
    print "Case #" + str(c + 1) + ": " + res
