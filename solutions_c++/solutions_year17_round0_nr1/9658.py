#include <iostream>
#include <stdbool.h>
#include <string>
using namespace std;

int main(int argc, char*argv[]) {
    int tests = 0;
    cin >> tests;
    int numFlip = 0;
    int i = 1;
    while (tests != 0) {
        string test = "";
        string fliper;
        cin >> test;
        cin >> fliper;
        const unsigned long testlen = test.length();
        const int fliperLen = stoi(fliper);

        // already happy
        if (test.find('-') == string::npos) {
            cout << "Case #" << i << ": " << 0 << endl;
            --tests;
            ++i;
            continue;
        }
        else { // not happy yet
            for (unsigned int j = 0; j < testlen; j++) {
                if (test[j] == '-') {
                    if (j + fliperLen > testlen) {
                        break;
                    }
                    for (unsigned int x = j; x < j + fliperLen; x++) {
                        if (test[x] == '+') {
                            test[x] = '-';
                        }
                        else if (test[x] == '-'){
                            test[x] = '+';
                        }
                    }
                    ++numFlip;
                }
            }
            if (test.find('-') == string::npos) {
                cout << "Case #" << i << ": " << numFlip << endl;
            }
            else {
                cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
            }
            --tests;
            ++i;
            numFlip = 0;
            continue;
        }
    }

//    bitset<9> b(string("101111000"));
//    cout << b[6] << endl;


    return 0;
}