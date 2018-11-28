#include <iostream>
#include <string>

using namespace std;

void printResult(int t, string s) {
    cout << "Case #" << t << ": " << s << endl;
}

int main(int argc, char **argv) {
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        string inputString;
        cin >> inputString;
        int nineIndex = inputString.size();
        int previousDigit = inputString.back() - '0';
        int borrow = false;
        for (int p = inputString.size() - 2; p >= 0; --p) {
            int digit = inputString[p] - '0';
            if (borrow) {
                digit--;
                borrow = false;
            }
            if (digit < 0) {
                borrow = true;
                digit = 9;
            }
            if (digit > previousDigit) {
                nineIndex = p + 1;
                digit--;
                if (digit < 0) {
                    digit = 9;
                    borrow = true;
                }
            }
            inputString[p] = digit + '0';
            previousDigit = digit;
        }
        for (int i = nineIndex; i < inputString.size(); ++i) {
            inputString[i] = '9';
        }
        int index = 0;
        for (int i = 0; i < inputString.size(); ++i) {
            if (inputString[i] != '0') { break; }
            index++;
        }
        printResult(t, inputString.substr(index));
    }
    return 0;
}