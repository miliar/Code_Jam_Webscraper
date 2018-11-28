#include <bits/stdc++.h>
using namespace std;

const int maxN = 1e2+100;

int n, k;
int m;
long long d[maxN][maxN];
int dist[maxN], velo[maxN];
double f[maxN];

struct pt{
	int u;
	double f;
};

struct cmp{
	bool operator()(pt x, pt y) {
		return x.f > y.f;
	}
};

priority_queue<pt, vector<pt>, cmp> heap;

pt gan(int u, double f) {
	pt x;
	x.u = u;
	x.f = f;
	return x;
}

void dijtra(int u) {
	for(int i=1; i<=n; i++)
		f[i] = 1.0*54687*1ll*6654*7945;
	f[u] = 0;
	heap.push(gan(u, 0));
	while (!heap.empty()) {
		u = heap.top().u;
		double time = heap.top().f;
		// printf("%d %.9lf\n", u, time);
		heap.pop();
		if (abs(time - f[u]) > 0.000001)
			continue;
		for(int v=1; v<=n; v++)
			if (d[u][v] <= dist[u]) {
				// cout << d[u][v] << endl;
				double ctime = time + 1.0*d[u][v] / (1.0*velo[u]);
				if (ctime < f[v]) {
					f[v] = ctime;
					heap.push(gan(v, f[v]));
				}
			}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for(int dem = 1; dem <= test; dem++) {
		printf("Case #%d: ", dem);
		int query;
		cin >> n >> query;
		for(int i=1; i<=n; i++) 
			scanf("%d %d", &dist[i], &velo[i]);
		for(int i=1; i<=n; i++)
			for(int j=1; j<=n; j++) {
				scanf("%lld", &d[i][j]);
				if (d[i][j] == -1)
					d[i][j] = 1ll*10000000*10000000;
			}
		for(int i=1; i<=n; i++)
			d[i][i] = 0;
		for(int k=1; k<=n; k++)
			for(int i=1; i<=n; i++)
				for(int j=1; j<=n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		// for(int i=1; i<=n; i++) {
		// 	for(int j=1; j<=n; j++) 
		// 		printf("%lld ", d[i][j]);
		// 	cout << endl;
		// }
		while (query>0) {
			int s, t;
			cin >> s >> t;
			dijtra(s);
			printf("%.9lf ", f[t]);
			query--;
		}
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
}