#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int t;
    string S;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> S;
        for (int a = 0; a < 18; ++a)
            for (int c = 0; c < S.length() - 1; ++c) {
                if (S[c] > S[c + 1]) {
                    S[c] -= 1;
                    while (++c < S.length())
                        S[c] = '9';
                }
            }
        if (S[0] == '0') {
            cout << "Case #" << i << ": " << S.substr(1) << endl;
        } else {
            cout << "Case #" << i << ": " << S << endl;
        }

    }
}