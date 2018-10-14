#!/usr/bin/python

from string import maketrans
import sys

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
alphabet = ''.join(alphabet)

key      = "y n f i c w l b k u o m x s e v z p d r j g t h a q".split(' ')
key      = ''.join(key)

encryptrans = maketrans(alphabet, key)
decryptrans = maketrans(key, alphabet)

if __name__ == "__main__":
    num_lines = int(sys.stdin.readline())
    count = 1
    for line in sys.stdin.readlines():
        if line.strip() == '':
            continue
        line = line.strip()

        answer = line.translate(decryptrans)
        print "Case #%d: %s" % (count, answer)
        count += 1
