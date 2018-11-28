#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
bool cakes[1005];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    ll T;
    cin >> T;
    for (ll t = 1; t <= T; t++) {
        string s;
        cin >> s;
        ll k;
        cin >> k;
        for (ll i = 0; i < s.size(); i++) {
            cakes[i] = (s[i] == '+');
        }
        ll cnt = 0;
        for (ll i = 0; i <= s.size()-k; i++) {
            if (!cakes[i]) {
                cnt++;
                for (ll j = 0; j < k; j++) {
                    cakes[i+j] = !cakes[i+j];
                }
            }
        }
        for (ll i = s.size()-k+1; i < s.size(); i++) {
            if (!cakes[i]) {
                cout << "Case #" << t << ": IMPOSSIBLE" << endl;
                goto esc;
            }
        }
        cout << "Case #" << t << ": " << cnt << endl;
        esc:;
    }
}
