#include <iostream>

using namespace std;

void solve(int e) {
    cout << "Case #" << e << ": ";

    int ans = 0;
    string s; int k; cin >> s >> k;
    for (int i = 0; i < int(s.size()); ++i) {
        if (s[i] == '-') {
            if (i > int(s.size()) - k) {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
            ++ans;

            for (int u = i; u < i+k; ++u) {
                if (s[u] == '-')
                    s[u] = '+';
                else
                    s[u] = '-';
            }
        }
    }

    cout << ans << endl;
}

int main() {
    int t; cin >> t;
    for (int e = 1; e <= t; ++e)
        solve(e);
}
