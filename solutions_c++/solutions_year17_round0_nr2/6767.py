#include <iostream>
#include <string>

using namespace std;

int main() {
    int numOfTestCase;
    cin >> numOfTestCase;

    for (int i = 1; i <= numOfTestCase; ++i) {
        string tidyNumber;
        cin >> tidyNumber;
        int currentPos = 0;
        for (size_t j = 1; j < tidyNumber.size(); ++j) {
            if (tidyNumber[j] > tidyNumber[currentPos]) {
                currentPos = j;
                continue;
            }
            if (tidyNumber[j] < tidyNumber[currentPos]) {
                string stringToFlip = tidyNumber.substr(currentPos, -1);
                string flippedString = stringToFlip; // To get correct size
                if (stringToFlip[0] == '0') {
                    flippedString[0] = '9';
                } else {
                    flippedString[0] -= 1;
                }
                for (size_t k = 1; k < stringToFlip.size(); ++k) {
                    flippedString[k] = '9';
                }
                tidyNumber = tidyNumber.substr(0, currentPos) + flippedString;
            }
        }
        if (tidyNumber[0] == '0') {
            tidyNumber = tidyNumber.substr(1);
        }
        cout << "Case #" << i << ": " << tidyNumber << endl;
    }
}
