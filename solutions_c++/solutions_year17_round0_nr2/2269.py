#include <iostream>

using namespace std;

string lastTidyNumber(string s) {
    int r = 1;
    while (s[r] >= s[r - 1]) {
        r++;
    }
    if (r >= s.size()) {
        return s;
    }
    int l = r - 1;
    while (s[l] == s[r - 1]) {
        l--;
    }
    l++;
    s[l]--;
    for (int i = l + 1; i < s.size(); ++i) {
        s[i] = '9';
    }
    if (l == 0 && s[l] == '0') {
        s = s.substr(1, s.size() - 1);
    }
    return s;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string s;
        cin >> s;
        cout << "Case #" << i + 1 << ": " << lastTidyNumber(s) << "\n";
    }
    return 0;
}
