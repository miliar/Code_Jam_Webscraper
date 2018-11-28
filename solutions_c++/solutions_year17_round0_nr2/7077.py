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
        ll n;
        cin >> n;
        for (ll i = 1; i < n; i *= 10) {
            ll low = n / i % 10;
            ll high = n / i / 10 % 10;
//            cout << "l " << low << " h " << high << endl;
            if (high > low) {
                n = n - n%(10*i) - 1;
            }
//            cout << n << endl;
        }
        cout << "Case #" << t << ": " << n << endl;
    }
}
