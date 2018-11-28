#include <iostream>
using namespace std;

void flip(char& c) {
    c = c == '-' ? '+' : '-';
}

int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas) {
        string s;
        int k;
        cin >> s >> k;
        int n = s.size();
        int ans = 0;
        for (int i = 0; i <= n - k; ++i) {
            if (s[i] == '-') {
                for (int j = 0; j < k; ++j)
                    flip(s[i + j]);
                ++ans;
            }
        }
        bool ok = true;
        for (int i = 0; i < n; ++i)
            if (s[i] == '-') {
                ok = false;
                break;
            }
        cout << "Case #" << cas << ": ";
        if (ok) {
            cout << ans << '\n';
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
}
