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
#define MAX 500

const int k = 2;
int n, m;
ii a[MAX], b[MAX];

int eval(ii p[MAX]) {
    int a = p[0].ff, b = p[0].ss;
    int c = p[1].ff, d = p[1].ss;
    if (d - a <= 720) return 2;
    if (b + 1440 - c <= 720) return 2;
    return 4;
}

int solve() {
    sort(a, a + n);
    sort(b, b + m);
    if (n + m < 2) {
        return 2;
    }
    if (n && m) {
        return 2;
    }
    if (n) return eval(a);
    return eval(b);
}

int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	    freopen("../../../../../../tst-files/inp.txt", "r", stdin);
	    freopen("../../../../../../tst-files/out.txt", "w", stdout);
	#endif
	int cases, caseNo = 0;
	cin >> cases;
	while (cases--) {
	    cin >> n >> m;
	    rep(i, n) cin >> a[i].ff >> a[i].ss;
	    rep(i, m) cin >> b[i].ff >> b[i].ss;
	    printf("Case #%d: %d\n", ++caseNo, solve());
	}
	return 0;
}

// lamphanviet@gmail.com
