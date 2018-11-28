#include <iostream>
using namespace std;

int getLength(char* number) {
    int length = 0;
    while(number[length] != '\0') length++;
    return length;
}

void findTidyNumber(char* number, int length) {
    for (int i = 0; i < length - 1; ++i) {
        if (number[i] > number[i + 1]) {
            number[i] = (number[i] == '0') ? '9' : number[i] - 1;
            for (int j = i + 1; j < length; ++j) {
                number[j] = '9';
            }
            return findTidyNumber(number, length);
        }
    }

    if (number[0] == '0') {
        for (int i = 0; i < length; ++i) {
            number[i] = number[i + 1];
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        char S [19] = {0,};
        cin >> S;
        int length = getLength(S);
        if (length != 1) findTidyNumber(S, length);
        cout << "Case #" << tc << ": " << S << endl;
    }
    return 0;
}