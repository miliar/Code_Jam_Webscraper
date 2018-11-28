#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

typedef pair <int, int> ii;

const int nil = 3030;
const int Maxm = 6060;
const int Maxn = 55;
const int Maxd = 4;
const int dy[Maxd] = {1, 0, -1, 0};
const int dx[Maxd] = {0, -1, 0, 1};
const int ch1[Maxd] = {1, 0, 3, 2};
const int ch2[Maxd] = {3, 2, 1, 0};

int T;
int R, C;
char B[Maxn][Maxn];
int cur, num[Maxn][Maxn];
bool tk[Maxn][Maxn][Maxd];
vector <ii> E;
vector <int> neigh[Maxm];
bool marked[Maxm];
vector <int> S;
int compnum, comp[Maxm];

void Clear()
{
	fill((bool*)tk, (bool*)tk + Maxn * Maxn * Maxd, false);
}

ii Get(int r, int c, int ang)
{
	if (tk[r][c][ang]) return ii(0, ang);
	if (B[r][c] == '#') return ii(0, ang);
	if (num[r][c] > 0) return ii(num[r][c], ang);
	tk[r][c][ang] = true;
	if (B[r][c] == '/') ang = ch1[ang];
	else if (B[r][c] == '\\') ang = ch2[ang];
	return Get(r + dy[ang], c + dx[ang], ang);
}

ii getLeft(int r, int c) { Clear(); return Get(r + dy[1], c + dx[1], 1); }

ii getRight(int r, int c) { Clear(); return Get(r + dy[3], c + dx[3], 3); }

ii getUp(int r, int c) { Clear(); return Get(r + dy[2], c + dx[2], 2); }

ii getDown(int r, int c) { Clear(); return Get(r + dy[0], c + dx[0], 0); }

int Not(int x) { return x >= nil? x - nil: x + nil; }

int getVert(ii p)
{
	if (p.first == 0) return 0;
	if (p.second % 2) return Not(p.first);
	return p.first;
}

void buildNeigh(bool rev)
{
	for (int i = 0; i < Maxm; i++)
		neigh[i].clear();
	for (int i = 0; i < E.size(); i++)
		if (rev) neigh[E[i].second].push_back(E[i].first);
		else neigh[E[i].first].push_back(E[i].second);
}

void dfsFirst(int v)
{
	marked[v] = true;
	for (int i = 0; i < neigh[v].size(); i++)
		if (!marked[neigh[v][i]]) dfsFirst(neigh[v][i]);
	S.push_back(v);
}

void dfsSecond(int v)
{
	marked[v] = true;
	for (int i = 0; i < neigh[v].size(); i++)
		if (!marked[neigh[v][i]]) dfsSecond(neigh[v][i]);
	comp[v] = compnum;
}

void Solve()
{
	E.clear();
	for (int i = 1; i <= R; i++)
		for (int j = 1; j <= C; j++)
			if (B[i][j] == '-' || B[i][j] == '|') {
				if (getLeft(i, j).first || getRight(i, j).first) E.push_back(ii(Not(num[i][j]), num[i][j]));
				if (getUp(i, j).first || getDown(i, j).first) E.push_back(ii(num[i][j], Not(num[i][j])));
			}
	for (int i = 1; i <= R; i++)
		for (int j = 1; j <= C; j++)
			if (B[i][j] == '.') {
				int h1 = getVert(getLeft(i, j)), h2 = getVert(getRight(i, j));
				int v1 = getVert(getUp(i, j)), v2 = getVert(getDown(i, j));
				if (h1 && h2) h1 = 0;
				else if (h1 == 0) h1 = h2;
				if (v1 && v2) v1 = 0;
				else if (v1 == 0) v1 = v2;
				if (h1 && v1) {
					E.push_back(ii(Not(h1), v1));
					E.push_back(ii(Not(v1), h1));
				} else if (h1)
					E.push_back(ii(Not(h1), h1));
				  else if (v1)
				  	E.push_back(ii(Not(v1), v1));
				  else { printf("IMPOSSIBLE\n"); return; }
			}
	buildNeigh(false); S.clear();
	fill(marked, marked + Maxm, false);
	fill(comp, comp + Maxm, 0); compnum = 0;
	for (int i = 0; i < E.size(); i++) {
		if (!marked[E[i].first]) dfsFirst(E[i].first);
		if (!marked[E[i].second]) dfsFirst(E[i].second);
		if (!marked[Not(E[i].first)]) dfsFirst(Not(E[i].first));
		if (!marked[Not(E[i].second)]) dfsFirst(Not(E[i].second));
	}
	fill(marked, marked + Maxm, false);
	buildNeigh(true);
	while (!S.empty()) {
		int v = S.back(); S.pop_back();
		if (!marked[v]) {
			compnum++;
			dfsSecond(v);
		}
	}
	for (int i = 0; i < E.size(); i++) {
		if (comp[E[i].first] == comp[Not(E[i].first)]) {
			printf("IMPOSSIBLE\n"); return;
		}
		if (comp[E[i].second] == comp[Not(E[i].second)]) {
			printf("IMPOSSIBLE\n"); return;
		}
	}
	printf("POSSIBLE\n");
	for (int i = 1; i <= R; i++) {
		for (int j = 1; j <= C; j++)
			if (B[i][j] == '-' || B[i][j] == '|')
				if (comp[num[i][j]] > comp[Not(num[i][j])]) printf("|");
				else printf("-");
			else printf("%c", B[i][j]);
		printf("\n");
	}
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		fill((char*)B, (char*)B + Maxn * Maxn, '#');
		scanf("%d %d", &R, &C);
		cur = 0;
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++) {
				scanf(" %c", &B[i][j]); num[i][j] = 0;
				if (B[i][j] == '-' || B[i][j] == '|') num[i][j] = ++cur;
			}
		printf("Case #%d: ", tc);
		Solve();
	}
	return 0;
}