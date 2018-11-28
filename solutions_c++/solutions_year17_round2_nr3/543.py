#include <bits/stdc++.h>
#define pb push_back
typedef long long ll;
const int N = 1e2 + 10;
const ll INF = 1e17;

using namespace std;

double f[N];
ll a[N][N], d[N][N], s[N], e[N];
int n, q, id, test;
bool vis[N];

void process(int start) {
	for (int i = 0; i < n; i++) f[i] = INF;
	f[start] = 0.0;
	memset(vis, 0, sizeof(vis));
	while (1) {
		double _min = INF;
		int pos;
		for (int i = 0; i < n; i++) {
			if (vis[i]) continue;
			if (f[i] < _min) {
				_min = f[i];
				pos = i;
			}
		}
		if (_min == INF) break;
		vis[pos] = true;
		for (int i = 0; i < n; i++) {
			if (vis[i]) continue;
			if (d[pos][i] <= e[pos]) {
				f[i] = min(f[i], f[pos] + 1.0 * (double) d[pos][i] / s[pos]);
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cout << fixed << setprecision(10);
	cin >> test;
	while (test--) {
		id++;
		cout << "Case #" << id << ": ";
		cin >> n >> q;
		for (int i = 0; i < n; i++) cin >> e[i] >> s[i];
		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++) {
				cin >> a[i][j];
				if (a[i][j] == -1) d[i][j] = INF;
				else d[i][j] = a[i][j];
			}	
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					if (d[i][j] > d[i][k] + d[k][j]) d[i][j] = d[i][k] + d[k][j];
		for (int i = 0; i < q; i++) {
			int u, v;
			cin >> u >> v;
			u--, v--;
			process(u);
			cout << f[v] << " ";
		}
		cout << endl;
	}
	return 0;
}