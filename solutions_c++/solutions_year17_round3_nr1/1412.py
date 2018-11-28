#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef pair<ll, ii> iii;

const int MAX = 1010;
const int INF = INT_MAX/3;
const int MAXLOG = 20;
const ll MOD = 1e9+7;
const double PI = acos(-1);

ll dp[MAX][MAX];

vector<ii> all;

ll go(int pos, int k) {
    if(k == 0) return 0;
    if(pos == all.size()) return -LLONG_MAX/3;
    ll &r = dp[pos][k];
    if(r == -1) {
//        cout << pos << " " << k << endl,
        r = -LLONG_MAX/3;
        r = max(go(pos+1, k), all[pos].second*all[pos].first + go(pos+1, k-1));
    }
    return r;
}

int cases;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    #ifdef FSOCIETY
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // FSOCIETY

    int t; cin >> t;
    while(t--) {
        int k, n; cin >> n >> k;
        all = vector<ii>(n);
        for(int i = 0; i < n; i++) {
            cin >> all[i].first >> all[i].second;
        }

        sort(all.rbegin(), all.rend());

        memset(dp, -1, sizeof dp);

        double ans = 0;
        for(int i = 0; i < n; i++) {
            ans = max(ans, PI*( all[i].first*all[i].first + 2*all[i].first*all[i].second + 2*go(i+1, k-1)));
//            cout << PI*( all[i].first*all[i].first) << endl;

//            cout << go(i+1, k-1) << endl;
        }
        cout << "Case #" << ++cases << ": ";
        cout << fixed << setprecision(10) << ans << "\n";
    }



}
