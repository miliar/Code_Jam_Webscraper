#include <stdio.h>
#include <iostream>
#include <vector>
#include <assert.h>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <memory.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, R, C;
char g[5][51];
int id[5][50];
vector<vector<int> > G;
int Not(int x) {
	if (x < n)
		return x + n;
	return x - n;
}
void addEdge(int u, int v) {
	G[u].push_back(v);
	G[v].push_back(u);
}
bool cvr[5][50];
int go(int r, int c, int dr, int dc) {
	r += dr;
	c += dc;
	if (r < 0 || r == R || c < 0 || c == C || g[r][c] == '#')
		return -1;
	cvr[r][c] = true;
	if (id[r][c] != -1)
		return id[r][c];
	return go(r, c, dr, dc);
}
int clr[10000];
bool DFS(int u, int c) {
	if (clr[u] != -1) {
		if (clr[u] != c)
			return false;
		return true;
	}
	clr[u] = c;
	for (int i = 0; i < G[u].size(); ++i)
		if (!DFS(G[u][i], !c))
			return false;
	return true;
}
int main()
{
	freopen("C:/Users/ASUS/Downloads/C-small-attempt0.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/C-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d:", tt);
		scanf("%d%d", &R, &C);
		memset(id, -1, sizeof(id));
		n = 0;
		vector<pair<int, int> > adj;
		for (int i = 0; i < R; ++i) {
			scanf("%s", g[i]);
			int last = -1;
			for (int j = 0; j < C; ++j) {
				if (g[i][j] == '-' || g[i][j] == '|') {
					id[i][j] = n++;
					if (last != -1)
						adj.push_back(make_pair(last, id[i][j]));
					last = id[i][j];
				}else if (g[i][j] == '#')
					last = -1;
			}
		}
		for (int j = 0; j < C; ++j) {
			int last = -1;
			for (int i = 0; i < R; ++i) {
				if (g[i][j] == '-' || g[i][j] == '|') {
					if (last != -1)
						adj.push_back(make_pair(last, id[i][j]));
					last = id[i][j];
				}
				else if (g[i][j] == '#')
					last = -1;
			}
		}
		G.clear();
		G.resize(n * 2);
		for (int i = 0; i < G.size(); ++i)
			addEdge(i, Not(i));
		for (int i = 0; i < adj.size(); ++i) {
			int u = adj[i].first;
			int v = adj[i].second;
			addEdge(u, Not(v));
			addEdge(Not(u), v);
		}
		vector<pair<int,int> > force;
		bool ok = true;
		for (int i = 0; i<R; ++i)
			for (int j = 0; j < C; ++j) {
				if (g[i][j] == '.') {
					int hor = max(go(i, j, 0, 1), go(i, j, 0, -1));
					int ver = max(go(i, j, 1, 0), go(i, j, -1, 0));
					if (max(hor, ver) == -1) {
						ok = false;
						i = j = 1e9;
						break;
					}
					if (hor == -1)
						force.push_back(make_pair(ver, 1));
					else if (ver == -1)
						force.push_back(make_pair(hor, 0));
					else
						addEdge(Not(ver), hor);
				}
			}
		memset(clr, -1, sizeof(clr));
		for (int i = 0; i < force.size(); ++i) {
			if (!DFS(force[i].first, force[i].second)) {
				ok = false;
				break;
			}
		}
		for (int i = 0; i < G.size(); ++i)
			if (clr[i] == -1)
				if (!DFS(i, 0)) {
					ok = false;
					break;
				}
		if (!ok) {
			puts(" IMPOSSIBLE");
			continue;
		}
		for (int i = 0; i<R; ++i)
			for (int j = 0; j<C; ++j)
				if (id[i][j] != -1) {
					if (clr[id[i][j]])
						g[i][j] = '|';
					else
						g[i][j] = '-';
				}
		memset(cvr, 0, sizeof(cvr));
		for(int i=0;i<R;++i)
			for(int j=0;j<C;++j)
				if (g[i][j] == '|') {
					go(i, j, -1, 0);
					go(i, j, 1, 0);
				}
				else if (g[i][j] == '-') {
					go(i, j, 0, -1);
					go(i, j, 0, 1);
				}
		for (int i = 0; i<R; ++i)
			for (int j = 0; j < C; ++j) {
				if (id[i][j] != -1 && cvr[i][j])
					ok = false;
				if (g[i][j] == '.' && !cvr[i][j])
					ok = false;
			}
		if (!ok) {
			puts(" IMPOSSIBLE");
			continue;
		}
		puts(" POSSIBLE");
		for (int i = 0; i < R; ++i)
			puts(g[i]);
	}
	return 0;
}