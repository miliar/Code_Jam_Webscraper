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

ll n, res;
vi digits;

bool steps(int i, int last, ll val, bool less) {
    if (i >= digits.size()) {
        if (res > n) {
            while(1);
        }
        res = max(res, val);
        return true;
    }
    if (less) {
        return steps(i + 1, 9, val * 10 + 9, less);
    }
    if (last <= digits[i]) {
        if (steps(i + 1, digits[i], val * 10 + digits[i], false)) {
            return true;
        }
    }
    for (int next = digits[i] - 1; next >= last; next--) {
        if (steps(i + 1, next, val * 10 + next, true)) {
            return true;
        }
    }

    return false;
}

ll solve() {
    digits.clear();
    ll nn = n;
    while (nn > 0) {
        digits.pb(nn % 10);
        nn /= 10;
    }
    reverse(all(digits));
    res = 1;
    steps(0, 0, 0, false);
    return res;
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
	    cin >> n;
	    cout << "Case #" << t + 1 << ": " << solve() << endl;
	}
	return 0;
}

// lamphanviet@gmail.com
