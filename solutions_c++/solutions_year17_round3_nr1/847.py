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
#define MAX 1005

int n, k;
ii a[MAX];
double f[MAX][MAX];

bool cmp(ii a, ii b) {
    return a.ff > b.ff;
}

double val(double r, double h) {
    return 2.0 * r * PI * h;
}

double solve() {
    sort(a + 1, a + n + 1, cmp);

    rep(i, n + 1) rep(j, n + 1) f[i][j] = 0;

    fr(i, 1, n) {
        f[i][1] = max(f[i - 1][1], PI * a[i].ff * a[i].ff + val(a[i].ff, a[i].ss));
    }

    fr(i, 1, n) {
        double s = val(a[i].ff, a[i].ss);
        fr(j, 2, k) {
            f[i][j] = max(f[i - 1][j], f[i - 1][j - 1] + s);
        }
    }
    double res = 0;
    fr(i, 1, n) res = max(res, f[i][k]);
    return res;
}

int main() {
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	    freopen("../../../../../../tst-files/inp.txt", "r", stdin);
	    freopen("../../../../../../tst-files/out.txt", "w", stdout);
	#endif

	int cases, caseNo = 0;
	cin >> cases;
	while (cases--) {
	    cin >> n >> k;
	    fr(i, 1, n) {
	        cin >> a[i].ff >> a[i].ss;
	    }

	    printf("Case #%d: %.12lf\n", ++caseNo, solve());
	}

	return 0;
}

// lamphanviet@gmail.com
