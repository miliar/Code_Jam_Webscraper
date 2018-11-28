#include <bits/stdc++.h>

using namespace std;

inline void solve() {
    string s;
    cin >> s;
    int n = s.size();
    int last = n;
    for (int i = n - 1; i > 0; i--)
        if (s[i] < s[i - 1]) {
            for (int j = i; j < last; j++)
                s[j] = '9';

            last = i;

            bool f = true;

            int j = i - 1;

            do {
                s[j]--;

                if (s[j] < '0') {
                    s[j] = '9';
                    j--;
                } else {
                    f = false;
                }
            } while (f);
        }

    cout << (s[0] == '0' ? s.substr(1) : s) << endl;
}

int main() {
    ios_base::sync_with_stdio(false);

#ifdef SCHEMTSCHIK
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else

#endif

    int T;
    cin >> T;

    for (int I = 0; I < T; I++) {
        cout << "Case #" << I + 1 << ": ";
        solve();
    }

    return 0;
}
