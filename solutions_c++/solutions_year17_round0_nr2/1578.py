#include <iostream>
using namespace std;

string countTidyNumber(string num) {
    string allNineNum = num;
    int posZero = -1;
    int size = num.size() - 1;

    for (int i = size ; i > 0 ; i--) {
        allNineNum[i] = '9';

        if (num[i] < num[i - 1]) {
            num = allNineNum;
            num[i - 1] = num[i - 1] - 1;
        }

        if (num[i - 1] == '0') {
            posZero = i - 1;
        } else {
            posZero = -1;
        }
    }

    return num.substr(posZero + 1);
}

int main() {
    int t;
    string n;

    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n;
        string ans = countTidyNumber(n);
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 1;
}
