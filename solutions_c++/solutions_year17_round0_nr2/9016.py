#include <iostream>
#include <sstream>

using namespace std;

void fixDigit(string &number) {
    for (int i = number.length() - 1; i >= 1; --i) {
        char digit = number[i];
        char digitL = number[i - 1];
        if (digit < digitL) {
            --number[i - 1];
            digit = number[i] = '9';
            for (int j = i + 1; j < number.length(); ++j) {
                char digitR = number[j];
                if (digitR < digit) {
                    digit = number[j] = '9';
                } else {
                    break;
                }
            }
        }
    }
}

int main() {
    int cases;
    int caseI = 1;
    unsigned long long result;
    string number;

    cin >> cases;
    cin.ignore();

    while (cases--) {
        getline(cin, number);
        fixDigit(number);
        if ( ! (istringstream(number) >> result) ) result = 0;
        cout << "Case #" << caseI++ << ": " << result << endl;
    }

    return 0;
}
