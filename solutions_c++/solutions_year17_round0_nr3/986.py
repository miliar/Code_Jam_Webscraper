#include<bits/stdc++.h>

#define show(x) cout << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef pair<double, ii> iii;

const int MAX = 200005;
const double EPS = 1e-5;
const int INF = INT_MAX;

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
        ll n, k; cin >> n >> k;
        set<ll, greater<ll>> q;
        map<ll, ll> cnt;
        q.insert(n);
        cnt[n] = 1;
        while(true) {
            ll u = *q.begin(); q.erase(q.begin());

            if(cnt[u] >= k) {
                cout << "Case #" << ++cases << ": ";
                if(u&1) {
                    cout << u/2  << " " << u/2 << "\n";
                } else {
                    cout << u/2  << " " << u/2-1 << "\n";
                }
                break;
            }

            k -= cnt[u];
            if(u&1) {
                cnt[ u/2 ] += cnt[u]*2;
                q.insert(u/2);
            } else {
                cnt[ u/2 ] += cnt[u];
                cnt[ (u-1)/2 ] += cnt[u];
                q.insert(u/2);
                q.insert((u-1)/2);
            }
        }
    }

}
