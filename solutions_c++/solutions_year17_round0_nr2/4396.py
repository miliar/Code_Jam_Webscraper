#include <bits/stdc++.h>

using namespace std;

string solve(string s) {
    int pos = (int)s.size();
    for (int i = (int) s.size() - 2; i >= 0; --i) {
        if (s[i] > s[i + 1]) {
            pos = i + 1;
            s[i] = (char)max((int)'0', s[i] - 1);
        }
    }
    for (int i = pos; i < (int)s.size(); ++i)
        s[i] = '9';
    std::reverse(s.begin(), s.end());
    while(s.size() > 1 && s.back() == '0')
        s.pop_back();
    std::reverse(s.begin(), s.end());
    return s;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::string s;
        cin >> s;
        cout << "Case #" << i << ": " << solve(s) << "\n";
    }
}
