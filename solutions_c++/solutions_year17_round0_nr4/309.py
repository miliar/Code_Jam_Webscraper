// .... .... .....!
// ...... ......!
// .... ....... ..... ..!
// ...... ... ... .... ... .... .....!
// ... .. ... .... ...?

#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
//#define endl '\n'

template<class P, class Q> inline void smin(P &a, Q b) { if (b < a) a = b; }
template<class P, class Q> inline void smax(P &a, Q b) { if (a < b) a = b; }

typedef long long ll;
typedef pair<int, int> pii;

////////////////////////////////////////////////////////////////////////////////

const int maxn = 100 + 10;

int n, m;
bool p[maxn][maxn], c[maxn][maxn];
bool col[maxn], row[maxn];
bool sum[2*maxn], dif[2*maxn];
vector<int> adj[2*maxn];
bool vis[2*maxn];
int match[2*maxn];

bool dfs(int u) {
	if(u == -1) return true;

	for(int v: adj[u]) if(!vis[v]) {
		vis[v] = true;
		if(dfs(match[v])) {
			match[v] = u;
			return true;
		}
	}

	return false;
}

void run() {
	cin >> n >> m;
	
	int ans = 0;
	int rem = n;

	rep(i, m) {
		char type;
		int x, y;
		cin >> type >> x >> y;
		x--, y--;
		
		if(type == 'x' || type == 'o') {
			col[x] = row[y] = true;
			c[x][y] = true;
			ans++;
			rem--;
		}

		if(type == '+' || type == 'o') {
			sum[x + y] = dif[x - y + n - 1] = true;
			p[x][y] = true;
			ans++;
		}
	}

	rep(i, n) rep(j, n) if(!sum[i + j] && !dif[i - j + n - 1]) adj[i + j].pb(i - j + n - 1);

	rep(i, 2*n-1) match[i] = -1;
	rep(i, 2*n-1) {
		memset(vis, false, sizeof vis);
		if(dfs(i)) ans++;
	}

	vector<pair<pii, char>> res;

	rep(i, 2*n-1) if(match[i] != -1) {
		int d = i - (n - 1), s = match[i];
		int x = (s + d) / 2, y = s - x;
		res.pb(make_pair(pii(x, y), c[x][y] ? 'o' : '+'));
		p[x][y] = true;
	}

	for(int x = 0, y = 0; rem--; ) {
		while(col[x]) x++;
		while(row[y]) y++;
		ans++;
		res.pb(make_pair(pii(x, y), p[x][y] ? 'o' : 'x'));
		x++, y++;
	}

	sort(all(res));
	int k = 0;
	rep(i, sz(res)) {
		if(i == 0 || (res[i].X != res[k-1].X))
			res[k++] = res[i];
		else
			res[k-1].Y = 'o';
	}
	res.resize(k);

	cout << ans << ' ' << sz(res) << endl;
	rep(i, sz(res)) cout << res[i].Y << ' ' << res[i].X.X + 1 << ' ' << res[i].X.Y + 1 << endl;

	memset(col, false, sizeof col);
	memset(row, false, sizeof row);
	memset(sum, false, sizeof sum);
	memset(dif, false, sizeof dif);
	memset(p, false, sizeof p);
	memset(c, false, sizeof c);
	rep(i, 2*n) adj[i].clear();
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		cerr << "running test #" << tc << ".. " << endl;

		cout << "Case #" << tc << ": ";
		run();
	}

	return 0;
}

