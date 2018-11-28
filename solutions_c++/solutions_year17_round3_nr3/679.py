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

int n, k;
double unit, a[MAX], b[MAX];

double solve() {
    double lo = 0, hi = 1.0, p = 0;
    rep(_, 100000) {
        double mid = (lo + hi) / 2;
        double sum = 0;
        rep(i, n) {
            if (a[i] < mid) {
                sum += mid - a[i];
                b[i] = mid;
            } else {
                b[i] = a[i];
            }
        }
        if (sum > unit) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    double res = 1.0;
    rep(i, n) res *= b[i];
    return res;
}

int main() {
	#ifndef ONLINE_JUDGE
	    freopen("../../../../../../tst-files/inp.txt", "r", stdin);
	    freopen("../../../../../../tst-files/out.txt", "w", stdout);
	#endif

	int cases, caseNo = 0;
	cin >> cases;
	while (cases--) {
	    cin >> n >> k;
	    cin >> unit;
	    rep(i, n) cin >> a[i];
	    printf("Case #%d: %.12lf\n", ++caseNo, solve());
	}

	return 0;
}

// lamphanviet@gmail.com
