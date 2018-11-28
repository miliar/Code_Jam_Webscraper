#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    //freopen("B-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    //ios::sync_with_stdio(false);
    //cin.tie(0);
    int tc; cin >> tc;
    for (int tci = 1; tci <= tc; ++tci) {
        string n; cin >> n;
        ll ans = 0; int mini = 9;
        for (int i = n.length()-1, j = 0; i >= 0; --i, ++j) {
            int d = n[i] - '0';
            //printf("\t%d_%d: %lld %d %d %lld\n", i, j, ans, mini, d, (ll)ceil(pow(10, j)));
            if (d <= mini) mini = d;
            else ans = (ll)ceil(pow(10, j)) - 1, mini = --d;
            //printf("\t%d_%d: %lld %d %d %lld\n", i, j, ans, mini, d, (ll)ceil(pow(10, j)));
            ans += d * (ll)ceil(pow(10, j));
            //printf("\t%d_%d: %lld %d %d %lld\n", i, j, ans, mini, d, (ll)ceil(pow(10, j)));
        }
        cout << "Case #" << tci << ": " << ans << endl;
    }
}
