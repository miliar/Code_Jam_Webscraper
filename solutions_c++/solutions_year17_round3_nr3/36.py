#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define REP(i,a) FOR(i,0,(int)(a)-1)
#define reset(a,b) memset(a,b,sizeof(a))
#define BUG(x) cout << #x << " = " << x << endl
#define PR(x,a,b) {cout << #x << " = "; FOR (_,a,b) cout << x[_] << ' '; cout << endl;}
#define CON(x) {cout << #x << " = "; for(auto i:x) cout << i << ' '; cout << endl;}
#define mod 1000000007
#define pi acos(-1)
#define eps 1e-9
#define pb push_back
#define sqr(x) (x) * (x)
#define _1 first
#define _2 second

int t;
int n, k;
double tot, pr[55], req, high, low;

bool ok(double x) {
	double rem = tot;
	REP (i, n) rem -= max(0.0, x - pr[i]);
	return rem >= -eps;
}

int main() {
	ios::sync_with_stdio(false);
	cin >> t;
	FOR (cas, 1, t) {
		cout << "Case #" << cas << ": ";
		cin >> n >> k >> tot;
		req = 0;
		REP (i, n) cin >> pr[i], req += 1 - pr[i];
		if (abs(req - tot) < eps) {
			cout << 1.0 << endl;
			continue;
		}
		high = 1;
		low = 0;
		REP (_, 1000) {
			double chs = (high + low) / 2;
			if (ok(chs)) low = chs;
			else high = chs;
		}
		double ans = 1;
		REP (i, n) ans *= max(pr[i], high);
		cout << setprecision(11) << ans << endl;
	}
}
