#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double dou;
const int MAXN = 1e3 + 10;
dou pi = 3.141592653589;


ll mrx(ll a, ll b) {return a < b ? b : a;}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    ll t, heights;
    cin >> t;
    while (t--) {
        ll n, k, ans = 0, mx = 0;
        cin >> n >> k;
        pair <ll, ll> pai[MAXN];
        for (int i = 0; i < n; i++) {
            ll rad, heights;
            cin >> rad >> heights;
            pai[i] = make_pair(2 * rad * heights, rad);
        }
        sort(pai, pai + n), reverse(pai, pai + n);
        for (int i = 0; i < n; i++) {
            ll rad = pai[i].second, l = 0, ans = 0;
            pair <ll, ll> specs[MAXN];
            for (int j = 0; j < n; j++)
                if (pai[j].second <= rad && j != i)
                    specs[l++] = make_pair(pai[j].first, pai[j].second);
            if (l > k - 2) {
                for (int j = 0; j < k - 1; j++)
                    ans += specs[j].first;
                ans += pai[i].first + rad * rad;
                mx = max(ans, mx);
            }
        }
        cout << "Case #" << ++heights << ": " << setprecision(9) << fixed << dou(dou(mx) * pi) << endl;
    }
    return 0;
}
