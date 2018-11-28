#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

int memo[20][10][2];
int from[20][10][2];
ll n;
vi d;

int pd(int curpos, int lastd, int lim) {
	if(curpos == d.size()) {
		return 1;
	} else if(memo[curpos][lastd][lim] != -1) {
		return memo[curpos][lastd][lim];
	} else {
		if(lim) {
			bool ok = false;
			int to;
			for(int i = d[curpos]; i >= lastd; i--) {
				if(pd(curpos + 1, i, lim and i == d[curpos])) {
					ok = true;
					to = i;
					break;
				}
			}
			if(ok) {
				from[curpos][lastd][lim] = to;
			}
			return memo[curpos][lastd][lim] = ok;
		}else {
			bool ok = false;
			int to;
			for(int i = 9; i >= lastd; i--) {
				if(pd(curpos + 1, i, 0)) {
					ok = true;
					to = i;
					break;
				}
			}
			if(ok) {
				from[curpos][lastd][lim] = to;
			}
			return memo[curpos][lastd][lim] = ok;
		}
	}
}

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		memset(memo, -1, sizeof memo);
		memset(from, -1, sizeof from);
		cin >> n;
		d.clear();
		while(n) {
			d.pb(n%10);
			n/=10;
		}
		reverse(d.begin(), d.end());
		pd(0, 0, 1);

		int last = 0;
		int lim = 1;
		ll ans = 0;
		for(int i = 0; i < d.size(); i++) {
			ans *= 10;
			ans+=from[i][last][lim];
			last = from[i][last][lim];
			lim = lim and last == d[i];
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
		
	
	return 0;
}
