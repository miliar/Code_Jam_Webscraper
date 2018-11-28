#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

const long long INF = (long long)1e12;
int N, Q;
int E[200], S[200];
int U[200], V[200];
int b[20000], hea[200], nex[20000], tot;
long long c[20000];
int b2[20000], hea2[200], nex2[20000], tot2;
double c2[20000];

long long dis[200][200];
double dis2[200];

int q[200];
bool vis[200];

void addedge(int v1, int v2, int d) {
	b[++tot] = v2; c[tot] = d;
	nex[tot] = hea[v1];
	hea[v1] = tot;
}

void addedge2(int v1, int v2, double d) {
	//cerr << v1 << ' ' << v2 << ' ' << d << endl;
	b2[++tot2] = v2; c2[tot2] = d;
	nex2[tot2] = hea2[v1];
	hea2[v1] = tot2;
}

void spfa(int v) {
	for (int i = 0; i < N; ++i) dis[v][i] = INF;
	dis[v][v] = 0;
	memset(vis, false, sizeof(vis));
	int h = 0, t = 1;
	q[0] = v; vis[v] = true;
	while (h != t) {
		for (int i = hea[q[h]]; i != 0; i = nex[i]) {
			int tmp = dis[v][q[h]] + c[i];
			if (tmp <= E[v] && tmp < dis[v][b[i]]) {
				dis[v][b[i]] = tmp;
				if (!vis[b[i]]) {
					vis[b[i]] = true;
					q[t] = b[i];
					t = (t + 1) % N;
				}
			}
		}
		vis[q[h]] = false;
		h = (h + 1) % N;
	}

	for (int i = 0; i < N; ++i) {
		if (i != v && dis[v][i] <= E[v]) addedge2(v, i, (double)dis[v][i] / (double)S[v]);
	}
}

void spfa2(int v) {
	for (int i = 0; i < N; ++i) dis2[i] = 1e12;
	dis2[v] = 0;
	memset(vis, false, sizeof(vis));
	int h = 0, t = 1;
	q[0] = v; vis[v] = true;
	while (h != t) {
		for (int i = hea2[q[h]]; i != 0; i = nex2[i]) {
			double tmp = dis2[q[h]] + c2[i];
			if (tmp < dis2[b2[i]]) {
				dis2[b2[i]] = tmp;
				if (!vis[b2[i]]) {
					vis[b2[i]] = true;
					q[t] = b2[i];
					t = (t + 1) % N;
				}
			}
		}
		vis[q[h]] = false;
		h = (h + 1) % N;
	}
}

void buildg() {
	for (int i = 0; i < N; ++i) {
		spfa(i);
	}
}

void work() {
	scanf("%d%d", &N, &Q);
	for (int i = 0; i < N; ++i) {
		scanf("%d%d", &E[i], &S[i]);
	}

	memset(hea, 0, sizeof(hea));
	memset(nex, 0, sizeof(nex));
	tot = 0;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			int d;
			scanf("%d", &d);
			if (d > -1) addedge(i, j, d);
		}
	}
	for (int i = 0; i < Q; ++i) {
		scanf("%d%d", &U[i], &V[i]);
		--U[i]; --V[i];
	}

	memset(hea2, 0, sizeof(hea2));
	memset(nex2, 0, sizeof(nex2));
	tot2 = 0;
	buildg();

	for (int i = 0; i < Q; ++i) {
		spfa2(U[i]);
		printf("%.8f", dis2[V[i]]);
		if (i != Q - 1) printf(" ");
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i+ 1);
		work();
	}
	return 0;
}
