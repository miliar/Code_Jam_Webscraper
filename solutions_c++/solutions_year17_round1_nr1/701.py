#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<string> vs;
const int MOD = 1e9 + 7;
const int di[] = { -1,0,1,0 };
const int dj[] = { 0,1,0,-1 };
#define INF 1000000000
#define mp make_pair

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		int n, m; cin >> n >> m;
		vs g(n);
		for (int i = 0; i < n; i++)
			cin >> g[i];
		vector<vb> vis(n, vb(m));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (g[i][j] != '?') {
					for (int k = j + 1; k < m && g[i][k] == '?'; k++)
						g[i][k] = g[i][j];
					for (int k = j - 1; k >= 0 && g[i][k] == '?'; k--)
						g[i][k] = g[i][j];
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (g[i][j] != '?') {
					for (int k = i + 1; k < n && g[k][j] == '?'; k++)
						g[k][j] = g[i][j];
					for (int k = i - 1; k >= 0 && g[k][j] == '?'; k--)
						g[k][j] = g[i][j];
				}
			}
		}

		cout << "Case #" << ++tt << ":" << endl;
		for (int i = 0; i < n; i++)
			cout << g[i] << endl;
	}
	//cin.ignore(), cin.get();
}
