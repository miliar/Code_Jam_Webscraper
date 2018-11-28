#include <iostream>
#include <string>
using namespace std;

string tidy(string s) {
    if (s.length() <= 1) {
        return s;
    }
    for (int i = s.length() - 1; i > 0; i--) {
        if (s[i] < s[i-1]) {
            for (int j = i; j < s.length(); j++) {
                s[j] = '9';
            }
            s[i-1] = s[i-1] - 1;
        }
    }
    if (s[0] == '0') {
        s = s.substr(1);
    }
    return s;
}

int main() {
    int t, m;
    string s;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> s;
        cout << "Case #" << i << ": " << tidy(s) << endl;
    }
    return 0;
}
