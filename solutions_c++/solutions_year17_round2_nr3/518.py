#include <bits/stdc++.h>
using namespace std;
const int maxn = 105;
int n, d[maxn][maxn], e[maxn], s[maxn];
long long f[maxn][maxn];
double z[maxn];
bool inq[maxn];

double spfa(int u, int v) {
	queue<int> Q;
	memset(inq, false, sizeof(inq));
	Q.push(u);
	inq[u] = true;
	for(int i = 1; i <= n; i++) z[i] = 1e17;
	z[u] = 0;
	while(!Q.empty()) {
		int now = Q.front(); Q.pop();
		for(int i = 1; i <= n; i++) {
			if(f[now][i] <= e[now]) {
				double t = (double)f[now][i] / s[now];
				if(z[i] > z[now] + t) {
					z[i] = z[now] + t;
					if(!inq[i]) {
						inq[i] = true;
						Q.push(i);
					}
				}
			}
		}
		inq[now] = false;
	}
	return z[v];
}

void solve_big(int cases) {
	int u, v, q;
	scanf("%d%d", &n, &q);
	for(int i = 1; i <= n; i++) scanf("%d%d", &e[i], &s[i]);
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			scanf("%d", &d[i][j]);
			f[i][j] = d[i][j] == -1 ? INT_MAX : d[i][j];
		}
	}
	for(int k = 1; k <= n; k++) {
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				if(f[i][j] > f[i][k] + f[k][j]) f[i][j] = f[i][k] + f[k][j];
			}
		}
	}
	vector<double> ans;
	while(q--) {
		scanf("%d%d", &u, &v);
		ans.push_back(spfa(u, v));
	}
	printf("Case #%d:", cases);
	for(double x : ans) {
		printf(" %.10f", x);
	}
	printf("\n");
}

int main() {
	//freopen("sample_in.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.ou.txt", "w", stdout);

	int T, cases = 0;
	
	scanf("%d", &T);
	while(T--) {
		//solve_small(++cases);
		solve_big(++cases);
	}
	return 0;
}
