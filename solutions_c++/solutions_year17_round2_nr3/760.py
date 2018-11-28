#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

#define LL long long
#define INF (1LL<<60)
#define MAXN 101
#define MAXQ 101

int T, nCase;
int N, Q;
double E[MAXN], S[MAXN];
LL dist[MAXN][MAXN];
double U[MAXQ], V[MAXQ];
double A[MAXQ];

void prep()
{
	for (int k=0;k<N;++k)
		for (int i=0;i<N;++i)
			for (int j=0;j<N;++j) {
				LL s = dist[i][k] + dist[k][j];
				if (s < dist[i][j])
					dist[i][j] = s;
			}
}

double t[MAXN];

void solv()
{
	prep();
	for (int qq = 0; qq < Q; ++ qq) {
		int u = U[qq], v = V[qq];
		bool visit[MAXN];
		for (int i=0;i<N;++i) {
			t[i] = INF;
			visit[i] = false;
		}
		t[u] = 0;
		while (!visit[v]) {
			int p = -1;
			double fastest = INF;
			for (int i=0;i<N;++i) {
				if (!visit[i] && t[i] < fastest) {
					fastest = t[i];
					p = i;
				}
			}
			if (p == v) break;
			for (int i=0;i<N;++i) {
				if (!visit[i] && dist[p][i] <= E[p] && t[p] + dist[p][i] / S[p] < t[i])
					t[i] = t[p] + dist[p][i] / S[p];
			}
			visit[p] = true;
		}
		A[qq] = t[v];
	}
}

int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> N >> Q;
		for (int i=0;i<N;++i) cin >> E[i] >> S[i];
		for (int i=0;i<N;++i) for(int j=0;j<N;++j) {
			cin >> dist[i][j];
			if (dist[i][j] < 0) dist[i][j] = INF;
		}
		for (int i=0;i<Q;++i) { cin >> U[i] >> V[i]; U[i]--; V[i] --; }

		solv();
		cout << "Case #" << nCase << ":";
		for (int i=0;i<Q;++i) printf(" %.6f", A[i]);
		cout << endl;
	}
	return 0;
}