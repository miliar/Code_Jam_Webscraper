#include "bits/stdc++.h"

using namespace std;

typedef long long ll;
typedef long double ld;


int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cout.precision(10);

    srand(unsigned(time(NULL)));

    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);

    int Tcase;
    cin >> Tcase;
    int cnt = 0;
    while (Tcase--) {
        ++cnt;
        string s;
        cin >> s;
        int k;
        cin >> k;
        int cur = 0;
        int ans = 0;
        while (true) {
            while (cur < s.size() && s[cur] == '+')
                ++cur;
            if (cur + k <= s.size()) {
                for (int i = cur; i < cur + k; ++i) {
                    s[i] = (s[i] == '+' ? '-' : '+');
                }
                ++ans;
            } else
                break;
        }
        bool ok = true;
        for (const auto &i : s)
            ok &= i == '+';
        cout << "Case #" << cnt << ": ";
        if (!ok)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << '\n';

    }

}

