from numpy import*

## Code jam 2012, question A. Substitution cypher.

filename = "A-small-attempt0.in.txt"
FILE = open(filename, "r")
N = int(FILE.readline())

A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
B = ["y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"]


for k in range(N):
    words = map(str, FILE.readline().split())
    translation = ""
    for i in range(len(words)):
        for j in range(len(words[i])):
            translation = translation+A[B.index(words[i][j])]
        translation = translation+" "
    print "Case #%d: %s"%(k+1, translation)
