#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define ull unsigned long long
#define ll long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI  3.1415926535897932385
#define EPS 1e-7
#define MOD 1000000007
#define INF 1500111222
#define MAX 500005

ll n, k;

void solve() {
    ll ways = 0;
    map<ll, ll> cnt;
    map<ll, ll>::iterator it;
    cnt[n] = 1;

    while (ways < k) {
        it = cnt.end(); it--;
        ll key = it->ff, val = it->ss;

        ll mini, maxi;
        if (key & 1) {
            mini = maxi = key / 2;
        } else {
            maxi = key / 2;
            mini = maxi - 1;
        }

        ways += val;
        if (ways >= k) {
            cout << maxi << " " << mini << endl;
            return;
        }
        cnt.erase(it);

        cnt[mini] += val;
        cnt[maxi] += val;
    }
}

int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	    freopen("../../../../../tst-files/inp.txt", "r", stdin);
	    freopen("../../../../../tst-files/out.txt", "w", stdout);
	#endif
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++) {
	    cin >> n >> k;
	    cout << "Case #" << t + 1 << ": ";
	    solve();
	}
	return 0;
}

// lamphanviet@gmail.com
