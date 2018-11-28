#include <bits/stdc++.h>
using namespace std;
#define pr(x) cout << #x << " = " << x << endl;
#define bug cout << "bugbug" << endl;
#define ppr(x, y) printf("(%d, %d)\n", x, y);
#define MST(a,b) memset(a,b,sizeof(a))
#define CLR(a) MST(a,0)
#define SQR(a) ((a)*(a))
#define PCUT puts("\n---------------")

typedef long long ll;
typedef double DBL;
typedef pair<int, int> P;
typedef unsigned int uint;
const int MOD = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int maxn = 1e2 + 4;
const int maxm = 1e3 + 4;
const double pi = acos(-1.0);


ll dis[maxn][maxn], E[maxn];
double cost[maxn][maxn], s[maxn];
int n, q;
void floyd(){
	for (int k = 1; k <= n; ++k)
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			if (dis[i][j] > E[i]) cost[i][j] = INF;
			else cost[i][j] = dis[i][j] / s[i];
	for (int k = 1; k <= n; ++k)
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
}
int main(){
	int ik, i, j, k, kase;
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> kase;
	for (ik = 1; ik <= kase; ++ik){
		cin >> n >> q;
		for (i = 1; i <= n; ++i) cin >> E[i] >> s[i];
		for (i = 1; i <= n; ++i)
			for (j = 1; j <= n; ++j){
				cin >> dis[i][j];
				if (dis[i][j] == -1) dis[i][j] = INF;
			} 
		floyd();
		printf("Case #%d:", ik);
		while(q--){
			int u, v;
			cin >> u >> v;
			printf(" %.7f", cost[u][v]);
		}
		puts("");
	}
	return 0;
}

