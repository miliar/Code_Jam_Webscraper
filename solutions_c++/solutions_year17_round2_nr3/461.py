#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

int E[N], S[N];
long long G[N][N];

const long long int inf = 1e12;
long double dista[N];

long double ask(int n) {
	int u, v;
	scanf("%d%d", &u, &v);
	for (int i = 0; i <= n; i ++) {
		dista[i] = inf;
	}
	dista[u] = 0;
	set<pair<long double, int>> kol;
	kol.insert(make_pair(0, u));
	while(!kol.empty()) {
		int x = kol.begin() -> second;
		kol.erase(kol.begin());
		for (int i = 1; i <= n; i ++) {
			if (G[x][i] <= E[x]) {
				long double czas = dista[x] + G[x][i] / (long double)S[x];
				if (czas < dista[i]) {
					kol.erase(make_pair(dista[i], i));
					dista[i] = czas;
					kol.insert(make_pair(dista[i], i));
				}
			}
		}
	}
	return dista[v];
}

vector<long double> test() {
	int n, q;
	scanf("%d%d", &n, &q);
	for (int i = 1; i <= n; i ++) {
		scanf("%d%d", E + i, S + i);
	}
	for (int i = 1; i <= n; i ++) {
		for (int j = 1; j <= n; j ++) {
			scanf("%lld", &G[i][j]);
			if (G[i][j] == -1)
				G[i][j] = inf;
			if (i == j) {
				G[i][j] = 0;
			}
		}
	}
	for (int k = 1; k <= n; k ++)
		for (int i = 1; i <= n; i ++) 
			for (int j = 1; j <= n; j ++) {
				G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
			}
	vector<long double> res;
	for (int i = 0; i < q; i ++) {
		res.push_back(ask(n));
	}
	return res;
}

void print_test() {
	auto v = test();
	for (auto x: v) {
		printf("%.10Lf ", x);
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		print_test();
		printf("\n");
	}
}
