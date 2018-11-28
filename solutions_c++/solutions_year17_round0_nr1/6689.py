#include <bits/stdc++.h>

using namespace std;

string s;
long long t, k;
long long result;

void solve() {
    result = 0;
    for (size_t i = 0; i <= s.size() - k; ++i) {
        if (s[i] == '-') {
            for (size_t j = i; j < i + k; ++j) {
                s[j] = (s[j] == '+' ? '-' : '+');
            }
            ++result;
        }
        //cerr << s << "\n";
    }
    for (size_t i = s.size() - k + 1; i < s.size(); ++i) {
        if (s[i] == '-') {
            result = -1;
            break;
        }
    }
}

int main()
{
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> s >> k;
        solve();
        cout << "Case #" << i+1 << ": ";
        if (result == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << result;
        }
        cout << "\n";
    }

    return 0;
}
