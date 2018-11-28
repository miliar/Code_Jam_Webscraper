#include <iostream>
#include <string>
using namespace std;

void flip(string &s, int i, int m) {
    for (int j = i; j < i+m; j++) {
        if (s[j] == '-') {
            s[j] = '+';
        } else {
            s[j] = '-';
        }
    }
}

string pancake(string s, int m) {
    int count = 0;
    for (int i = 0; i <= s.length() - m; i++) {
        if (s[i] == '-') {
            flip(s, i, m);
            count++;
        }
    }
    for (int i = s.length() - m; i < s.length(); i++) {
        if (s[i] == '-') {
            return "IMPOSSIBLE";
        }
    }
    return to_string(count);
}

int main() {
    int t, m;
    string s;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> s >> m;
        cout << "Case #" << i << ": " << pancake(s, m) << endl;
    }
    return 0;
}
