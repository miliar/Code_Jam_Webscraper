#include <iostream>
#include <queue>

using namespace std;

//map<pair<int, pair<int, bool>>, int64_t>
string solve(string& s) {
    bool fixed = true;
    while (fixed) {
        fixed = false;
        for (size_t i = 1; i < s.size(); ++i) {
            if (s[i] < s[i-1]) {
                fixed = true;
                for (size_t j = i; j < s.size(); ++j) {
                    s[j] = '9';
                }
                s[i - 1] = s[i - 1] - 1;
                break;
            }
        }
    }
    while (s[0] == '0')
        s = s.substr(1);
    if (s == "")
        s = "0";
    return s;
}
int64_t solve(const string& s, int pos = 0, int next = '0', bool exceed = true) {
    if (pos == s.size()) return 1;
    int64_t result = 0;
    if (exceed) {
        for (int i = next; i < s[pos]; ++i) {
            result += solve(s, pos + 1, i, false);
        }
        result += solve(s, pos + 1, s[pos], true);
    } else {
        for (int i = next; i <= '9'; ++i) {
            result += solve(s, pos + 1, i, false);
        }
    }
    return result;
}

int main() {
    int T = 10000;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }
}