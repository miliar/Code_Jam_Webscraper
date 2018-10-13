__author__ = 'regis'

TRANS = str.maketrans("yeqjpmslcknribtahwfougdxvz", "aozurlngeibtdhwyxfckjvsmpq")

def translate(input):
    return input.translate(TRANS)

FILENAME = "A-small-attempt2"
if __name__ == '__main__':
    with open('dataset/' + FILENAME + '.in', 'r') as f:
        nbcases = int(f.readline())
        for i in range(1, nbcases + 1):
            t = translate(f.readline())
            print("Case #{i}: {text}".format(i=i, text=t))
