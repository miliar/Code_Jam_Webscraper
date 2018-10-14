# Google Code Jam
# Speaking in Tongues
# Dan Collins 2012

"""
    First make a dictionary with the mappings from googlerese to English
"""

# This is the provided input and output strings
# They will be used to create the dictionary
i1 = list("ejp mysljylc kd kxveddknmc re jsicpdrysi")
i2 = list("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
i3 = list("de kr kd eoya kw aej tysr re ujdr lkgc jv")

o1 = list("our language is impossible to understand")
o2 = list("there are twenty six factorial possibilities")
o3 = list("so it is okay if you want to just give up")

mapping = {'y':'a', 'e':'o', 'q':'z', 'a':'y', 'o':'e', 'z':'q'} # Holds the mapping data (googlerese -> english)

# This repeats three times on the input data, creating the dictionary
j = 0
for i in i1:
    mapping[i] = o1[j]
    j += 1

j = 0
for i in i2:
    mapping[i] = o2[j]
    j += 1

j = 0
for i in i3:
    mapping[i] = o3[j]
    j += 1

"""
    Now use the dictionary on the input file
"""

inFile = open('A-small-attempt3.in') # Get input
count = int(inFile.readline()) # Get number of entries

for i in range(1, count+1): # Loop through all of the entries
    entry = list(inFile.readline()) # Get a line from the file as a list
    outputLine = "Case #" # Will hold a single line of output text
    outputLine += str(i)
    outputLine += ": "
    for letter in entry: # Loop through all of the letters
        if (letter == '\n'):
            outputLine += '\n' # This wont be in the dictionary
        else:
            outputLine += mapping[letter] # Find the input letter in the dictionary, and add the value to the output string

    f = open("output.txt", 'a')
    f.write(outputLine)
    f.close()

