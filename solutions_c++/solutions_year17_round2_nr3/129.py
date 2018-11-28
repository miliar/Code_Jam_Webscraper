#include<cstdio>
#include<cassert>
#include<cstring>
#include<map>
#include<set>
#include<time.h>
#include<algorithm>
#include<stack>
#include<queue>
#include<utility>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include <limits>

using namespace std;

typedef pair <int, int> ii;
const long long INF = 1e9 + 7;
const long long INF9 = 1e9 + 9;

long long gcd(long long b, long long s){
	return (s != 0) ? gcd(s, b%s) : b;
}

long long pw(long long a, long long b, long long c) {
	if (b == 0) return 1;
	else if (b == 1) return a%c;
	else {
		long long A = pw(a, b / 2, c);
		A = (A*A) % c;
		if (b & 1) A = (A*a) % c;
		return A;
	}

}

const int N = 102;

long long E[N], S[N];
long long D[N][N];
double d[N][N];

long long dist[N];
typedef pair <long long, long long> ll;

void Do(int st, int n) {
	priority_queue <ll> q;

	for (int i = 1; i <= n; i++) dist[i] = INF;
	dist[st] = 0;
	q.push(ll(-dist[st], st));

	while (!q.empty()) {
		ii p = q.top(); q.pop();
		int u = p.second;
		if (dist[u] < -p.first) continue;
		for (int i = 1; i <= n; i++) {
			if (D[u][i] != -1 && dist[u] + D[u][i] < dist[i]) {
				dist[i] = dist[u] + D[u][i];
				q.push(ll(-dist[i], i));
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		if (dist[i] <= E[st]) {
			d[st][i] = (((double)dist[i]) / ((double)S[st]));
		}
		else
			d[st][i] = INF*INF;
	}
}

void solve() {
	int n, q;
	scanf("%d %d", &n, &q);

	for (int i = 1; i <= n; i++)
		scanf("%lld %lld", E + i, S + i);
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			scanf("%lld", &D[i][j]);

	for (int i = 1; i <= n; i++)
		Do(i, n);

	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

	for (int i = 0; i < q; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		printf("%.9lf ", d[u][v]);
	}
	puts("");
}


int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int R = 1; R <= T; R++) {
		printf("Case #%d: ", R);
		solve();
	}

}