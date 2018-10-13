'''
Created on Apr 14, 2012

@author: John Bui
'''

translation = {'y':'a',
               'n':'b',
               'f':'c',
               'i':'d',
               'c':'e',
               'w':'f',
               'l':'g',
               'b':'h',
               'k':'i',
               'u':'j',
               'o':'k',
               'm':'l',
               'x':'m',
               's':'n',
               'e':'o',
               'v':'p',
               'z':'q',
               'p':'r',
               'd':'s',
               'r':'t',
               'j':'u',
               'g':'v',
               't':'w',
               'h':'x',
               'a':'y',
               'q':'z',
               ' ':' ',
               '\n':'\n'
               };

# Global variable for number of cases    
caseCount = 0;

# Main method that runs the whole program
def main():
    # Declare new list that receives a list of strings from reading the input file lines
    inputFile = readFile("A-small-attempt0.in.txt");
    # Declare new empty list that will contain the translation
    outputFile = list();
    
    # FOR every line in inputFile, translate. Increment
    for caseNumber in range(0, caseCount):
        outputFile.append("Case #" + str(caseNumber + 1) + ": " + translate(inputFile[caseNumber]));
        caseNumber += 1;
        
    # Save onto my file
    writeFile(outputFile);

# Convert Googlerese letters to English
def translate(inputLine):
    # Declare empty string
    translatedLine = "";
    
    # FOR every 'char' in inputLine, translate
    for char in inputLine:
        translatedLine += translation[char];
        
    # Return Googlerese to English translated line
    return translatedLine;


# Read input file
def readFile(fileName):
    # Read file
    inputFile = open(fileName);
    
    # Declare new list
    inputList = list();
    
    # Declare number of cases from reading first line
    global caseCount; 
    caseCount = int(inputFile.readline());
    
    # FOR every line in inputFile, add to new list inputList
    for i in range(0, caseCount):
        line = inputFile.readline();
        inputList.append(line);
        i += 1;
        
    # Return list of lines from input files
    return inputList;
    
# Write translation of Googlerese to English
def writeFile(translatedList):
    # Open my output file
    file = open("translatedFile.txt", "w");
    
    # Write onto my file
    file.writelines(translatedList);
    
    # Close
    file.close();
    
# Run main method    
if __name__ == "__main__":
    main()