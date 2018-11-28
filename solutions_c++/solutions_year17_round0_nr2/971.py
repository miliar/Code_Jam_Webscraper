#include <string>
#include <iostream>
using namespace std;

string solve(string s) {
    if (s.size() == 1) return s;
    for (int i = 0; i < s.size()-1; i ++) {
        if (s[i] > s[i+1]) {
            s[i] --;
            for (int j = i+1; j < s.size(); j ++) {
                s[j] = '9';
            }
            if (i == 0 && s[i] == '0') {
                s = s.substr(1, s.size()-1);
            }
            break;
        }
    }
    return s;
}

bool check(string s) {
    if (s.size() == 1) return true;
    for (int i = 0; i < s.size()-1; i ++) {
        if (s[i] > s[i+1]) return false;
    }
    return true;
}

int main() {
    int T, kase = 0; cin >> T;
    while (T--) {
        string s; cin >> s;
        while (!check(s)) {
            s = solve(s);
        }
        cout << "Case #" << ++kase << ": " << s << '\n';
    }
    return 0;
}
