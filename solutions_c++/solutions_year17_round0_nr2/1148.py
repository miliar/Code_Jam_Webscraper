#include <bits/stdc++.h>
using namespace std;

string S;
long long N;
long long f[20][10][2][2];
// [i][last][isGreater][nonZero]

long long cntTidy(long long n) {
	stringstream ss; ss << n; string s = ss.str(); int m = (int)s.size(); s = ' ' + s;
	memset(f, 0, sizeof f);
	f[0][0][0][0] = 1;
	for (int i = 1; i <= m; ++i) for (int j = 0; j <= 9; ++j) for (int gr = 0; gr < 2; ++gr) for (int zr = 0; zr < 2; ++zr) {
		if (!f[i-1][j][gr][zr]) continue;
		int l = j, r = 9; if (!gr) r = s[i] - '0';
		for (int nxt = l; nxt <= r; ++nxt) {
			int nj = nxt, ngr = gr, nzr = zr;
			if (!gr && nxt < r) ngr = 1; if (!zr && nxt) nzr = 1;
			f[i][nj][ngr][nzr] += f[i-1][j][gr][zr];
		}
		//cerr << i << ' ' << j << ' ' << gr << ' ' << zr << ' ' << f[i][j][gr][zr] << endl;
	}
	long long ans = 0;
	for (int j = 0; j <= 9; ++j) ans += f[m][j][1][1];
	return ans;
}

int nc;
void solve() {
	cin >> N;
	long long ans = cntTidy(N + 1);
	long long l = 2, r = N + 1;
	while(l != r) {
		long long mid = ((l + r) >> 1);
		if (cntTidy(mid) >= ans) r = mid;
		else l = mid + 1;
	}
	printf("Case #%d: %lld\n", ++nc, l - 1);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	while(T--)
		solve();
}
