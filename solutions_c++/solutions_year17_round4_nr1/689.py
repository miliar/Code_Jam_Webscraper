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

int t, n, p, cnt[4], val;

int main() {
	ios::sync_with_stdio(false);
	cin >> t;
	FOR (cas, 1, t) {
		cout << "Case #" << cas << ": ";
		cin >> n >> p;
		reset(cnt, 0);
		REP (i, n) cin >> val, cnt[val % p]++;
		int ans = cnt[0];
		if (p == 2) ans += (cnt[1] + 1) / 2;
		else if (p == 3) {
			int tmp = min(cnt[1], cnt[2]);
			cnt[1] -= tmp;
			cnt[2] -= tmp;
			ans += tmp;
			ans += cnt[1] / 3 + cnt[2] / 3;
			cnt[1] %= 3;
			cnt[2] %= 3;
			if (cnt[1] + cnt[2] > 0) ans++;
		} else if (p == 4) {
			ans += cnt[2] / 2;
			cnt[2] %= 2;
			int tmp = min(cnt[1], cnt[3]);
			cnt[1] -= tmp;
			cnt[3] -= tmp;
			ans += tmp;
			if (cnt[2] && cnt[1] > 1) ans++, cnt[2] = 0, cnt[1] -= 2;
			if (cnt[2] && cnt[3] > 1) ans++, cnt[2] = 0, cnt[3] -= 2;
			ans += cnt[1] / 4;
			ans += cnt[3] / 4;
			cnt[1] %= 4;
			cnt[3] %= 4;
			if (cnt[1] + cnt[2] + cnt[3] > 0) ans++;
		} else assert(false);
		cout << ans << endl;
	}
}