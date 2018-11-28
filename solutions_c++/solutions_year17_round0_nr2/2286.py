#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string solve(string s) {
    for (int i = 0; i < s.size() - 1; i++) {
        if (s[i] > s[i + 1]) {
            int p = i;
            while (p > 0 && (s[p-1] == s[p] || s[p] == '0')) {
                p--;
            }

            s[p]--;
            p++;
            while (p < s.size()) {
                s[p++] = '9';
            }                

            if (s[0] == '0') {
                s = s.substr(1, s.size() - 1);
            }
            break;
        }
    }

    return s;
}
            

int main() {
    int tests;

    cin >> tests;

    for (int test = 1; test <= tests; test++) {
        string s;
        cin >> s;
        string ans = solve(s);
        cout << "Case #" << test << ": " << ans << endl;
    }

    return 0;
}
