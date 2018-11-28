#include <iostream>
#include <string>

using namespace std;

string removeStartingZeroes (string number) {
    int i = 0;

    while (number[i] == '0') {
        i++;
    }

    return number.substr(i, number.size());
}

int main () {
    int testCases;
    string number;

    cin >> testCases;
    for (int curCase = 1; curCase <= testCases; curCase++) {
        cin >> number;

        for (int i = 0; i < static_cast<int>(number.size()) - 1; i++) {
            if (number[i] > number[i+1]) {
                number[i]--;
                for (int j = i+1; j < static_cast<int>(number.size()); j++) {
                    number[j] = '9';
                }
                i = -1;
            }
        }

        cout << "Case #" << curCase << ": " << removeStartingZeroes(number) << endl;
    }

    return 0;
}