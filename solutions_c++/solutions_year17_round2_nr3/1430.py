#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
#define DBG(x) cout<<#x<<" = "<<x<<";\n"


using namespace std;
int dx[] = { 0,0,-1,1,1,-1,1,-1 };
int dy[] = { 1,-1,0,0,1,1,-1,-1 };
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
vector<pii> adj[110];
double E[110];
double S[110];
const double eps = 0.0000000128;
double dp_q[110][110];
int vis[110][110];
int N;
double floyd[110][110];

double query(int u , int asb, int v) {
	if (vis[u][asb] > 0) {
		return dp_q[u][asb];
	}
	vis[u][asb] = 1;
	double minval = (double)1000000000 * (double)150;
	dp_q[u][asb] = minval;
	if (E[u] >= floyd[u][v] && floyd[u][v] != -1) {
		minval = (double)floyd[u][v] / S[u];
	}

	for (int nb = 0; nb < N; nb++) {
		if (nb == u || nb == v)continue;
		if (E[u] >= floyd[u][nb] && floyd[u][nb] != -1) {
			double val = (double)floyd[u][nb] / S[u] + query(nb, u, v);

			if (val < minval) {
				minval = val;
			}
		}
	}
	dp_q[u][asb] = minval;
	return minval;
}
void solve() {
	int Q,v,u;
	cin >> N >> Q;
	for (int i = 0; i < N; i++) {
		cin >> E[i] >> S[i];
	}
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			floyd[j][i] = -1;
			cin >> v;
			if (v == -1)continue;
			adj[j].push_back(pii(i, v));
			floyd[j][i] = v;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (floyd[i][k] == -1 || floyd[k][j] == -1)continue;
				double v = floyd[i][k] + floyd[k][j];
				if (v < floyd[i][j] || floyd[i][j] == -1) {
					floyd[i][j] = v;
				}
				
			}
		}
	}
	for (int i = 0; i < Q; i++) {
		if (i)cout << ' ';
		cin >> u >> v; u--; v--;
		memset(vis, 0, sizeof(vis));
		cout <<setprecision(10)<<fixed<< query(u,u,v);
	}
	
}
int main() {
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	for (int i = 1; i <= T; i++) {
		if (i == 7) {
			i = 7;
		}
		cout << "Case #" << i << ": ";
		solve();
		cout<< endl;
	}
	return 0;
}