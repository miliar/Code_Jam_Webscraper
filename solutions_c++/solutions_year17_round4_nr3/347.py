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

int t, n, m, vst[55][55][4], ans[55][55], canr[55][55][2], canc[55][55][2], canb[55][55][2], r, c, b, nr, nc, nb;
string grid[55];
queue<int> qr, qc, qb;
vector<pair<int, pair<int, int> > > v, adj[55][55][2];

bool valid(int r, int c) {
	return r >= 0 && c >= 0 && r < n && c < m && grid[r][c] != '#';
}

void proc(int r, int c, int b) {
	if (grid[r][c] == '/') {
		int tmpb = 1;
		if (b == 0 || b == 3) tmpb = 0;
		v.pb({tmpb, {r, c}});
	} else if (grid[r][c] == '\\') {
		int tmpb = 1;
		if (b == 0 || b == 1) tmpb = 0;
		v.pb({tmpb, {r, c}});
	} else v.pb({b % 2, {r, c}});
	if (grid[r][c] == '/') {
		vst[r][c][3 - b] = 1;
		if (b == 0) nr = r, nc = c - 1, nb = 1;
		if (b == 1) nr = r + 1, nc = c, nb = 0;
		if (b == 2) nr = r, nc = c + 1, nb = 3;
		if (b == 3) nr = r - 1, nc = c, nb = 2;
		if (valid(nr, nc) && !vst[nr][nc][nb]) {
			qr.push(nr);
			qc.push(nc);
			qb.push(nb);
			vst[nr][nc][nb] = 1;
		}
	} else if (grid[r][c] == '\\') {
		if (b == 0) nr = r, nc = c + 1, nb = 3, vst[r][c][1] = 1;
		if (b == 1) nr = r - 1, nc = c, nb = 2, vst[r][c][0] = 1;
		if (b == 2) nr = r, nc = c - 1, nb = 1, vst[r][c][3] = 1;
		if (b == 3) nr = r + 1, nc = c, nb = 0, vst[r][c][2] = 1;
		if (valid(nr, nc) && !vst[nr][nc][nb]) {
			qr.push(nr);
			qc.push(nc);
			qb.push(nb);
			vst[nr][nc][nb] = 1;
		}
	} else {
		if (b == 0) nr = r + 1, nc = c, nb = 0, vst[r][c][2] = 1;
		if (b == 1) nr = r, nc = c - 1, nb = 1, vst[r][c][3] = 1;
		if (b == 2) nr = r - 1, nc = c, nb = 2, vst[r][c][0] = 1;
		if (b == 3) nr = r, nc = c + 1, nb = 3, vst[r][c][1] = 1;
		if (valid(nr, nc) && !vst[nr][nc][nb]) {
			qr.push(nr);
			qc.push(nc);
			qb.push(nb);
			vst[nr][nc][nb] = 1;
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin >> t;
	FOR (cas, 1, t) {
		cout << "Case #" << cas << ": ";
		cin >> n >> m;
		REP (i, n) REP (j, m) REP (k, 2) adj[i][j][k].clear();
		REP (i, n) cin >> grid[i];
		while (!qr.empty()) qr.pop(), qc.pop(), qb.pop();
		reset(ans, -1);
		reset(vst, 0);
		reset(canr, -1);
		reset(canc, -1);
		reset(canb, -1);

		REP (i, n) REP (j, m) REP (k, 2) if (grid[i][j] == '.' || grid[i][j] == '|' || grid[i][j] == '-') if (!vst[i][j][k]) {
			v.clear();
			// cout << i << ' ' << j << ' ' << k << endl;
			qr.push(i); qc.push(j); qb.push(k); qr.push(i); qc.push(j); qb.push(k + 2);
			vst[i][j][k] = vst[i][j][k + 2] = 1;
			while (!qr.empty()) {
				r = qr.front(); qr.pop();
				c = qc.front(); qc.pop();
				b = qb.front(); qb.pop();
				proc(r, c, b);
			}
			// BUG(v.size());
			// for (auto pp: v) cout << pp._1 << ' ' << pp._2._1 << ' ' << pp._2._2 << endl;
			int cnt = 0, rr = -1, cc = -1, bb = -1;
			for (auto qq: v) {
				b = qq._1;
				r = qq._2._1;
				c = qq._2._2;
				if (grid[r][c] == '|' || grid[r][c] == '-') if (rr != r || cc != c || bb != b) {
					cnt++;
					rr = r;
					cc = c;
					bb = b;
				}
			}
			if (cnt != 1) continue;
			for (auto pp: v) {
				b = pp._1;
				r = pp._2._1;
				c = pp._2._2;
				canr[r][c][b] = rr;
				canc[r][c][b] = cc;
				canb[r][c][b] = bb;
			}
			// BUG(canr[1][2][1]);
		}
		// BUG(canr[1][2][1]);
		// BUG(canc[1][2][1]);
		// BUG(canb[1][2][1]);
		while (!qr.empty()) qr.pop(), qc.pop(), qb.pop();
		reset(vst, 0);
		bool flag = false;

		REP (i, n) REP (j, m) if (grid[i][j] != '#') {
			if (canr[i][j][0] == -1 && canr[i][j][1] == -1) {
				flag = true;
				// cout << i << ' ' << j << endl;
			}
			else if (canr[i][j][0] == -1) {
				r = canr[i][j][1];
				c = canc[i][j][1];
				b = canb[i][j][1];
				if (ans[r][c] != -1 && ans[r][c] != b) flag = true;
				ans[r][c] = b;
				qr.push(r); qc.push(c); qb.push(b);
				if (b) grid[r][c] = '-';
				else grid[r][c] = '|';
			} else if (canr[i][j][1] == -1) {
				r = canr[i][j][0];
				c = canc[i][j][0];
				b = canb[i][j][0];
				if (ans[r][c] != -1 && ans[r][c] != b) flag = true;
				ans[r][c] = b;
				qr.push(r); qc.push(c); qb.push(b);
				if (b) grid[r][c] = '-';
				else grid[r][c] = '|';
			} else {
				nr = canr[i][j][1];
				nc = canc[i][j][1];
				nb = canb[i][j][1];
				r = canr[i][j][0];
				c = canc[i][j][0];
				b = canb[i][j][0];
				if (nr == r && nc == c) {
					if (nb == b) {
						if (ans[r][c] != -1 && ans[r][c] != b) flag = true;
						ans[r][c] = b;
						if (b) grid[r][c] = '-';
						else grid[r][c] = '|';
					}
					continue;
				}
				adj[nr][nc][1 - nb].pb({b, {r, c}});
				adj[r][c][1 - b].pb({nb, {nr, nc}});
			}
		}
		// BUG(adj[0][1][0].size());
		// BUG(qr.size());
		while (!qr.empty()) {
			r = qr.front(); qr.pop();
			c = qc.front(); qc.pop();
			b = qb.front(); qb.pop();
			if (vst[r][c][b]) continue;
			vst[r][c][b] = 1;
			for (auto pp: adj[r][c][b]) {
				// BUG("asdfasf");
				nr = pp._2._1;
				nc = pp._2._2;
				nb = pp._1;
				// if (r == 0 && c == 1 && b == 0) BUG(nr), BUG(nc), BUG(nb);
				if (ans[nr][nc] != -1 && ans[nr][nc] != nb) flag = true;
				ans[nr][nc] = nb;
				if (nb) grid[nr][nc] = '-';
				else grid[nr][nc] = '|';
				qr.push(nr); qc.push(nc); qb.push(nb);
			}
		}
		REP (i, n) REP (j, m) if (grid[i][j] == '-' || grid[i][j] == '|') if (ans[i][j] == -1) {
			ans[i][j] = 0;
			qr.push(i);
			qc.push(j);
			qb.push(0);
			while (!qr.empty()) {
				r = qr.front(); qr.pop();
				c = qc.front(); qc.pop();
				b = qb.front(); qb.pop();
				if (vst[r][c][b]) continue;
				vst[r][c][b] = 1;
				for (auto pp: adj[r][c][b]) {
					// BUG("asdfasf");
					nr = pp._2._1;
					nc = pp._2._2;
					nb = pp._1;
					// if (r == 0 && c == 1 && b == 0) BUG(nr), BUG(nc), BUG(nb);
					if (ans[nr][nc] != -1 && ans[nr][nc] != nb) flag = true;
					ans[nr][nc] = nb;
					if (nb) grid[nr][nc] = '-';
					else grid[nr][nc] = '|';
					qr.push(nr); qc.push(nc); qb.push(nb);
				}
			}
		}
		REP (i, n) REP (j, m) if (grid[i][j] != '#') {
			if (canr[i][j][1] != -1 && canr[i][j][0] != -1) {
				nr = canr[i][j][1];
				nc = canc[i][j][1];
				nb = canb[i][j][1];
				r = canr[i][j][0];
				c = canc[i][j][0];
				b = canb[i][j][0];
				if (ans[nr][nc] != nb && ans[r][c] != b) flag = true;
			}
		}
		if (flag) cout << "IMPOSSIBLE" << endl;
		else {
			cout << "POSSIBLE" << endl;
			REP (i, n) cout << grid[i] << endl;
		}
	}
}