def speakingInTongues(inFilename, outFilename, codeFilename, writeToFile=0):
    """GCJ2012 - Qualification: A. Speaking in Tongues"""
    # Open output file, if needed
    if writeToFile:
        outFile = open(outFilename, 'w')

    Goog2Eng = dict({' ' : ' '})
    # Initialize stuff required across test cases
    with open(codeFilename) as codeFile:
        code = codeFile.readlines()

    for item in code:
        key, val = [x for x in item.split()]
        #print(key, val)
        Goog2Eng[key] = val

    Goog2EngTrans = str.maketrans(Goog2Eng)
    #print(len(Goog2EngTrans))
    #for key in Goog2EngTrans.keys():
    #   print(chr(key), chr(Goog2EngTrans[key]))
    #return

    #if(Goog2EngTrans == None):
    #    Goog2Eng = dict({'y' : 'a', 'e' : 'o', 'q' : 'z'})
    #    Goog2EngTrans = str.maketrans(Goog2Eng)

    # Read input file
    with open(inFilename) as inFile:
        # Read number of test cases T
        T = int(inFile.readline())
        #print("T = " + str(T))
        
        # For each test case t:
        for t in range(T):
            # Read line in Googlerese G
            G = inFile.readline().rstrip('\n')

            # Translate G into English S
            #S = G
            #S = repeat('?', len(G))

            S = G.translate(Goog2EngTrans)

            # Prepare and write output
            outStr = "Case #{t}: {S}".format(t=t+1, S=S)
            if writeToFile:
                print(outStr, file=outFile)
            print(outStr)

def getGoog2EngMap(gFilename, sFilename):
    """Creates map from Googlereese to English using corresponding files"""
    Goog2EngTrans = dict()
    
    # Read input files
    with open(gFilename) as gFile, open(sFilename) as sFile:
        # Read number of test cases T
        T = int(gFile.readline())
        #print("T = " + str(T))
        
        # For each test case t:
        for t in range(T):
            # Read Googlereese
            G = gFile.readline().rstrip('\n')
            
            # Read English
            S = sFile.readline().rstrip('\n')

            # Create translation table and merge
            tab = str.maketrans(G, S)
            Goog2EngTrans = dict(list(Goog2EngTrans.items()) + list(tab.items()))
            #print(G)
            #print(S)
            #print(len(Goog2EngTrans))
            #for key in Goog2EngTrans.keys():
            #    print(chr(key), chr(Goog2EngTrans[key]))

    # Add known mappings, in case they were not covered
    Goog2EngTrans[ord('y')] = ord('a')
    Goog2EngTrans[ord('e')] = ord('o')
    Goog2EngTrans[ord('q')] = ord('z')
    Goog2EngTrans[ord('z')] = ord('q')
                
    return Goog2EngTrans
    
# Make translation table
#Goog2EngTrans = getGoog2EngMap("A-sample-G.in", "A-sample-S.in")
#print(len(Goog2EngTrans))
#for key in Goog2EngTrans.keys():
#    print(chr(key), chr(Goog2EngTrans[key]))

# Run on sample input
#speakingInTongues("A-sample.in", "A-sample.out", "A-codebook.dat", 1)
speakingInTongues("A-small-attempt0.in", "A-small-attempt0.out", "A-codebook.dat", 1)

