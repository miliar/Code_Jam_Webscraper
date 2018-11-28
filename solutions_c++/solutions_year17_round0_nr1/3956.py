#include <iostream>
#include <string>

using namespace std;

void printResult(int t, int moves) {
    cout << "Case #" << t << ": " << moves << endl;
}

void printImpossible(int t) {
    cout << "Case #" << t << ": IMPOSSIBLE" << endl;
}

int main(int argc, char **argv) { int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        string inputString;
        cin >> inputString;
        int strSize = inputString.size();
        int flipSize;
        cin >> flipSize;
        int flipMoves = 0;
        bool impossible = false;
        for (int i = 0; i < strSize; ++i) {
            if (inputString[i] == '-') {
                // must flip
                if ((i + flipSize) > strSize) {
                    impossible = true;
                    break;
                }
                flipMoves++;
                for (int j = 0; j < flipSize; ++j) {
                    if (inputString[i+j] == '-') {
                        inputString[i+j] = '+';
                    } else {
                        inputString[i+j] = '-';
                    }
                }
            }
        }
        if (impossible) {
            printImpossible(t);
        } else {
            printResult(t, flipMoves);
        }
    }
}