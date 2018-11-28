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
#define eps 1e-20
#define pb push_back
#define sqr(x) (x) * (x)
#define _1 first
#define _2 second

int t;
long long n, k, r, h;
pair<long long, long long> p[1111];
vector<long long> v;

int main() {
	ios::sync_with_stdio(false);
	cin >> t;
	FOR (cas, 1, t) {
		cout << "Case #" << cas << ": ";
		cin >> n >> k;
		REP (i, n) {
			cin >> r >> h;
			p[i] = {r * r, h * r * 2};
		}
		sort(p, p + n);
		long long ans = 0;
		FOR (i, k - 1, n - 1) {
			long long tmp = p[i]._1 + p[i]._2;
			v.clear();
			REP (j, i) v.pb(p[j]._2);
			sort(v.begin(), v.end());
			REP (j, k - 1) tmp += v.back(), v.pop_back();
			ans = max(ans, tmp);
		}
		cout << setprecision(11) << ans * pi << endl;
	}
}
