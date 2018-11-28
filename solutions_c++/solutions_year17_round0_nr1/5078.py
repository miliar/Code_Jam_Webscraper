#include <iostream>
#include <string>

using namespace std;

int acquireFlips();
bool flip(string & pancakeRow, int index, int amountFlip);

int main() {
    int numCases, numFlips;
    cin >> numCases;
    for(int currentCase = 1; currentCase <= numCases; currentCase++) {
        numFlips = acquireFlips();
        cout << "Case #" << currentCase << ": ";
        if(numFlips == -1) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << numFlips << endl;
        }
    }
    return 0;
}

int acquireFlips() {
    string pancakeRow;
    int amountFlip;
    cin >> pancakeRow >> amountFlip;
    int numFlips = 0;

    bool flipResult;
    for(int index = 0; index < pancakeRow.size(); index++) {
        if(pancakeRow[index] == '-') {
            flipResult = flip(pancakeRow, index, amountFlip);
            if(!flipResult) {
                return -1;
            }
            ++numFlips;
        }
    }
    return numFlips;
}

bool flip(string & pancakeRow, int index, int amountFlip) {
    if(amountFlip > pancakeRow.size() - index) {
        return false;
    }

    for(int count = 0; count < amountFlip; count++) {
        if(pancakeRow[index + count] == '-') {
            pancakeRow[index + count] = '+';
        }
        else {
            pancakeRow[index + count] = '-';
        }
    }
    return true;
}

// O(nk), where k->n, so potentially O(n^2).