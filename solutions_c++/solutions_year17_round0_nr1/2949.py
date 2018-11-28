#include <bits/stdc++.h>

using namespace std;

using ll = long long;

inline void inv(char& c) {
    c = c == '+' ? '-' : '+';
}

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    srand(time(0));

#ifdef HOME
    freopen("/home/acarus/input.txt", "r", stdin);
    freopen("/home/acarus/output.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    for (int test_case = 1; test_case <= t; ++test_case) {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0;
        int pos = 0;
        while (pos < s.size()) {
            while (pos < s.size() && s[pos] == '+') ++pos;
            if (pos + k - 1 < s.size()) {
                for (int i = pos; i < pos + k; ++i) inv(s[i]);
                ++ans;
            }
            ++pos;
        }

        cout << "Case #" << test_case << ": ";
        if (s.find('-') == string::npos) {
            cout << ans;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}