#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    unsigned short i, j, k, numberOfInputs, numberOfFlips, inputSize, currentSize;
    string inputString, currentString;
    queue <string> allStrings;
    queue <unsigned short> allSizes;
    bool isPossible;

    cin >> numberOfInputs;

    for (i = 0; i < numberOfInputs; i++) {
        cin >> inputString;
        allStrings.push(inputString);
        cin >> inputSize;
        allSizes.push(inputSize);
    }

    for (i = 0; i < numberOfInputs; i++) {
        isPossible = true;
        numberOfFlips = 0;

        currentString = allStrings.front();
        allStrings.pop();

        currentSize = allSizes.front();
        allSizes.pop();

        for (j = 0; j < currentString.size(); j++) {

            if (currentString[j] == '-')
            {
                if (j + currentSize > currentString.size())
                {
                    isPossible = false;
                    break;
                }

                numberOfFlips++;

                for (k = 0; k < currentSize; k++)
                {
                    if (currentString[j + k] == '-')
                        currentString[j + k] = '+';
                    else
                        currentString[j + k] = '-';
                }
            }
        }

        if (isPossible)
            cout << "Case #" << i + 1 << ": " << numberOfFlips << endl;

        else
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
