#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair <int, int> ii;

const int Maxn = 105;
const int Maxm = 215;
const int MaxN = 2 * Maxm + 2;
const int Inf = 1000000000;

struct pos {
	char ch; int a, b;
	pos(char ch = '?', int a = 0, int b = 0): ch(ch), a(a), b(b) {}
};

int t;
int n, m;
char B[Maxn][Maxn];
bool okrow[MaxN], okcol[MaxN], okdiag1[MaxN], okdiag2[MaxN];
int N1, R1[MaxN][MaxN];
int N2, R2[MaxN][MaxN];
vector <int> neigh1[MaxN], neigh2[MaxN];
int par[MaxN], flow[MaxN];

int getFlow(int N, vector <int> neigh[], int R[][MaxN])
{
	fill(flow, flow + N, 0); flow[0] = Inf;
	priority_queue <ii> Q; Q.push(ii(flow[0], 0));
	while (!Q.empty()) {
		int v = Q.top().second, f = Q.top().first; Q.pop();
		if (flow[v] != f) continue;
		for (int i = 0; i < neigh[v].size(); i++) {
			int u = neigh[v][i];
			if (min(f, R[v][u]) > flow[u]) {
				flow[u] = min(f, R[v][u]); par[u] = v;
				Q.push(ii(flow[u], u));
			} 
		}
	}
	if (!flow[N - 1]) return 0;
	int v = N - 1;
	int res = flow[v];
	while (v) {
		int u = par[v];
		R[u][v] -= res; R[v][u] += res;
		v = u;
	}
	return res;
}

void addEdge(vector <int> neigh[], int R[][MaxN], int a, int b, int cap)
{
	neigh[a].push_back(b); neigh[b].push_back(a);
	R[a][b] = cap;
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		int mf = 0;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				B[i][j] = '.';
		fill(okrow, okrow + n, true); fill(okcol, okcol + n, true);
		fill(okdiag1, okdiag1 + 2 * n, true); fill(okdiag2, okdiag2 + 2 * n, true); 
		while (m--) {
			char ch; int r, c; scanf(" %c %d %d", &ch, &r, &c); r--; c--;
			B[r][c] = ch;
			if (ch == '+' || ch == 'o') { mf++; okdiag1[r - c + n] = okdiag2[r + c] = false; }
			if (ch == 'x' || ch == 'o') { mf++; okrow[r] = okcol[c] = false; }
		}
		N1 = n + n + 2;
		for (int i = 0; i < N1; i++) {
			neigh1[i].clear();
			for (int j = 0; j < N1; j++)
				R1[i][j] = 0;
		}
		for (int i = 0; i < n; i++) if (okrow[i]) {
			addEdge(neigh1, R1, 0, i + 1, 1);
			for (int j = 0; j < n; j++) if (B[i][j] == '.' || B[i][j] == '+') if (okcol[j])
				addEdge(neigh1, R1, i + 1, n + j + 1, 1);
		}
		for (int j = 0; j < n; j++) if (okcol[j])
			addEdge(neigh1, R1, n + j + 1, N1 - 1, 1);
		int d = n + n;
		N2 = d + d + 2;
		for (int i = 0; i < N2; i++) {
			neigh2[i].clear();
			for (int j = 0; j < N2; j++)
				R2[i][j] = 0;
		}
		for (int i = 0; i < d; i++) {
			if (okdiag1[i]) addEdge(neigh2, R2, 0, i + 1, 1);
			if (okdiag2[i]) addEdge(neigh2, R2, d + i + 1, N2 - 1, 1);
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) if (B[i][j] == '.' || B[i][j] == 'x') if (okdiag1[i - j + n] && okdiag2[i + j])
				addEdge(neigh2, R2, i - j + n + 1, d + i + j + 1, 1);
		int f;
		while ((f = getFlow(N1, neigh1, R1)) != 0) mf += f;
		while ((f = getFlow(N2, neigh2, R2)) != 0) mf += f;
		vector <pos> res;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				bool plus = R1[n + j + 1][i + 1] > 0;
				bool iks = R2[d + i + j + 1][i - j + n + 1] > 0;
				if (plus + iks == 2 || plus + iks > 0 && B[i][j] != '.')
					res.push_back(pos('o', i, j));
				else if (plus) res.push_back(pos('x', i, j));
				else if (iks) res.push_back(pos('+', i, j));
			}
		printf("Case #%d: %d %d\n", tc, mf, res.size());
		for (int i = 0; i < res.size(); i++)
			printf("%c %d %d\n", res[i].ch, res[i].a + 1, res[i].b + 1);
	}
	return 0;
}