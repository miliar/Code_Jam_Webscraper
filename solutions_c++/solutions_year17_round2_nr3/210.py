#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <ld, int> ldi;

const int Maxn = 105;
const ll Inf = 1000000000000000000ll;

int T;
int n, q;
int E[Maxn], S[Maxn];
ll dist[Maxn][Maxn];
ld tim[Maxn][Maxn];

void Calc(int r, ld res[])
{
	fill(res, res + Maxn, 1e30l); res[r] = 0;
	priority_queue <ldi> Q; Q.push(ldi(0, r));
	while (!Q.empty()) {
		int v = Q.top().second; ld d = -Q.top().first; Q.pop();
		if (d != res[v]) continue;
		for (int i = 1; i <= n; i++) if (dist[v][i] <= E[v]) {
			ld add = ld(dist[v][i]) / S[v];
			if (d + add < res[i]) {
				res[i] = d + add; Q.push(ldi(-res[i], i));
			}
		}
	}
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &n, &q);
		for (int i = 1; i <= n; i++)
			scanf("%d %d", &E[i], &S[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				int d; scanf("%d", &d);
				if (d == -1) dist[i][j] = i == j? 0: Inf;
				else dist[i][j] = d;
			}
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
		for (int i = 1; i <= n; i++)
			Calc(i, tim[i]);
		printf("Case #%d:", tc);
		while (q--) {
			int u, v; scanf("%d %d", &u, &v);
			cout << " " << fixed << setprecision(10) << tim[u][v];
		}
		cout << endl;
	}
	return 0;
}