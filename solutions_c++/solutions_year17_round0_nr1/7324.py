#include <iostream>
#include <vector>
#include <string>

using namespace std;

void Solve() {
    string s;
    getline(cin, s, '\n');
    size_t pos = s.find(' ');
    int k = atoi(s.substr(pos + 1).c_str());
    s = s.substr(0, pos);

    int ans = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            for (int j = 0; j < k; ++j) {
                if (i + j == s.size()) {
                    cout << "IMPOSSIBLE";
                    return;
                } else {
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
                }
            }
            ++ans;
        }
    }
    cout << ans;
}

int main() {
    string s;
    getline(cin, s, '\n');
    int t = atoi(s.c_str());
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        Solve();
        cout << endl;
    }
    return 0;
}
