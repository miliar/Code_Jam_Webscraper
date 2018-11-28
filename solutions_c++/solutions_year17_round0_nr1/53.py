#include <stdlib.h>

#include <string>
#include <iostream>

using namespace std;

inline char flip(char x) {
    return x == '+' ? '-' : '+';
}

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << i << ": ";

        int c = 0;
        for (int i = 0; i + k <= s.size(); i++) {
            if (s[i] == '-') {
                c++;
                for (int j = 0; j < k; j++) {
                    s[i+j] = flip(s[i+j]);
                }
            }
        }
        bool flag = false;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                flag = true;
            }
        }
        if (flag) {
            cout << "IMPOSSIBLE";
        } else {
            cout << c;
        }
        cout << endl;
    }
}
