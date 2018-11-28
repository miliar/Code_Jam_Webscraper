//Input
//
//The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).
//
//Output
//
//For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.
//
//Limits
//
//1 ≤ T ≤ 100.
//Every character in S is either + or -.
//2 ≤ K ≤ length of S.
//Small dataset
//
//2 ≤ length of S ≤ 10.
//Large dataset
//
//2 ≤ length of S ≤ 1000.
//Sample
//
//
//Input
//
//Output
//
//3
//---+-++- 3
//+++++ 4
//-+-+- 4
//
//Case #1: 3
//Case #2: 0
//Case #3: IMPOSSIBLE

#include <iostream>
#include <list>
#include <string>

using namespace std;

char flipIt(char pancake) {
    char newSide = '+';
    if (pancake == '+') {
        newSide = '-';
    }
    
    return newSide;
}

string flip(string pancakesOriginal, int flipIndex, int flipCount) {
    string newPancakes(pancakesOriginal);
    
    for (int i = 0; i < flipCount; i++) {
        newPancakes[flipIndex + i] = flipIt(newPancakes[flipIndex + i]);
    }
    
    return newPancakes;
}

int findTopmostWrongPancake(string pancakes) {
    if (pancakes[0] == '-') {
        return -1;
    }
    
    for (int i = 0; i < pancakes.size(); i++) {
        if (pancakes[i] == '-') {
            return i;
        }
    }
    
    return -1;
}

int findFirstBlankPancake(string pancakes) {
    int first = -1;
    
    for (int i = 0; i < pancakes.size(); i++) {
        if (pancakes[i] == '-') {
            first = i;
            break;
        }
    }
    
    return first;
}

int countFlips(string pancakes, int flipper_capacity) {
    string pancakesCopy(pancakes);
    
    int flips = 0;
    int lastFlipIndex = -1;
    
    int firstBlank = findFirstBlankPancake(pancakesCopy);
    
    while (firstBlank != -1) {
        int pancakes_count = (int) pancakesCopy.size();
        
        // There must always be flipper_capacity pancakes being flipped
        if (pancakes_count - firstBlank < flipper_capacity) {
            firstBlank = (pancakes_count - flipper_capacity);
        }
        
        //cout << "  Current pancakes " << pancakesCopy << endl;
        //cout << "  Flipping from " << firstBlank << ", " << flipper_capacity << " at a time" << endl;
        
        if (firstBlank == lastFlipIndex) {
            //cout << "  LOOP FOUND. ABORT" << endl;
            flips = -1;
            break;
        }
        
        pancakesCopy = flip(pancakesCopy, firstBlank, flipper_capacity);
        
        flips++;
        lastFlipIndex = firstBlank;
        
        firstBlank = findFirstBlankPancake(pancakesCopy);
    }
    
    return flips;
}

int main(int argc, const char * argv[]) {
    
    int t;
    cin >> t;
    cin.ignore();
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        
        string pancakes;
        cin >> pancakes;
        
        int flipper_capacity;
        cin >> flipper_capacity;
        
        int flips = countFlips(pancakes, flipper_capacity);
        
        if (flips == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << flips << endl;
        }
    }
    
    return 0;
}
