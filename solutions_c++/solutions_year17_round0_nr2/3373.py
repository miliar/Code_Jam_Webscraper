#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

void printSolution(const string &num) {
    if (num.size() == 1) {
        cout << num << endl;
        return;
    }

    string s = num;
    for (int i = s.size() - 1; i > 0; --i) {
        if (s[i] - '0' >= s[i - 1] - '0') {
            continue;
        }

        if (s[i - 1] == '0') {
            for (int j = i - 2; j <= 0; ++j) {
                if (s[j] > '0') {
                    s[j] = s[j] - 1;
                    for (int k = j + 1; k < s.size(); ++k) {
                        s[k] = '9';
                    }
                    break;
                }
            }

        } else {
            s[i - 1] = s[i - 1] - 1;
        }
        for (int j = i; j < s.size(); ++j) {
            s[j] = '9';
        }
    }

    cout << (s[0] == '0' ? s.substr(1) : s) << endl;
}

int main(int argc, char *argv[]) {
    int t;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string n;
        cin >> n;
        cout << "Case #" << i << ": ";
        printSolution(n);
    }

    return 0;
}