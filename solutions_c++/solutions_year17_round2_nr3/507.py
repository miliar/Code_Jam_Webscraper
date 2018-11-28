/*
 * GCJ 2017 round 1B
 * Task: B. Stable Neigh-bors
 */
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <bitset>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const double INF = 1e99;
const int MAXN = 101;

int n;
int maxHorseDist[MAXN];
int speed[MAXN];
int distGraph[MAXN][MAXN];
int query[MAXN][2];
double g[MAXN][MAXN];

double ds[MAXN];
int ps[MAXN], pr[MAXN], cap[MAXN];

void dijkstra(int root, int speed, int capacity)
{
	for (int i = 0; i < n; i++) {
		ps[i] = 0; pr[i] = -1;
		ds[i] = INF;
	}
	ds[root] = 0;
	cap[root] = capacity;
	while (1) {
		int bi = -1;
		double mdist = INF;
		for (int i = 0; i < n; i++) if (!ps[i] && ds[i] < mdist) {
			mdist = ds[i];
			bi = i;
		}
		if (bi == -1) return;
		g[root][bi] = min(g[root][bi], ds[bi]);
		ps[bi] = 1;
		for (int i = 0; i < n; i++) {
			if (distGraph[bi][i] == -1 || distGraph[bi][i] > cap[bi]) continue;
			double ncost = ds[bi] + distGraph[bi][i] / double(speed);
			if (!ps[i] && ds[i] > ncost) {
				pr[i] = bi;
				ds[i] = ncost;
				cap[i] = cap[bi] - distGraph[bi][i];
			}
		}
	}
}


vector<double> solve()
{
	vector<double> result;
	
	int q;
	scanf("%d%d", &n, &q);
	
	FOR(i, n) scanf("%d%d", maxHorseDist + i, speed + i);
	FOR(i, n) FOR(j, n) scanf("%d", &distGraph[i][j]);
	
	// compute time graph from distance graph:
	FOR(i, n) FOR(j, n) g[i][j] = INF;
	FOR(i, n) dijkstra(i, speed[i], maxHorseDist[i]);
	// run Floyd:
	FOR(k, n) FOR(i, n) FOR(j, n)
		g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
	
	FOR(i, q) {
		int from, to;
		scanf("%d%d", &from, &to);
		result.push_back(g[from - 1][to - 1]);
	}
	return result;
}

int main(void)
{
	//freopen("/home/vesko/gcj/C.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		vector<double> answers = solve();
		printf("Case #%d: ", tc);
		REP(i, answers) {
			if (i) printf(" ");
			printf("%.6lf", answers[i]);
		}
		printf("\n");
	}
	return 0;
}
