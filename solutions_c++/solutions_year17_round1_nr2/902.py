// OI.cpp : Defines the entry point for the console application.

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

int T, n, p;
vector<int> r;
vector<vector<int>> q;
vector<vector<pair<int, int>>> v;

const int MAX_NODE_NUM = 100010;
struct edge
{
	int v;
	edge *next;
	edge(int _v, edge *_next) :v(_v), next(_next) {}
} *e[MAX_NODE_NUM] = { NULL };
int s, t, ans = 0;// , F[MAX_NODE_NUM][MAX_NODE_NUM] = { 0 }, Q[MAX_NODE_NUM];
map<int, int> Q, pre, visited;
map<pair<int, int>, int>R, F;
//int R[MAX_NODE_NUM][MAX_NODE_NUM];
//int F[MAX_NODE_NUM][MAX_NODE_NUM];
//int pre[MAX_NODE_NUM];
//bool visited[MAX_NODE_NUM];

bool Find_Augmenting_Path()
{
	//memset(visited, false, sizeof(visited));
	visited.clear();
	Q[0] = s;
	pre[s] = -1;
	visited[s] = true;
	for (int head = 0, tail = 1; head<tail; head++)
	{
		int k = Q[head];
		for (edge *p = e[k]; p; p = p->next)
			if (!visited[p->v] && R[make_pair(k,p->v)]>0)
			{
				visited[p->v] = true;
				pre[p->v] = k;
				if (p->v == t) return true;
				Q[tail++] = p->v;
			}
	}
	return false;
}

void Augment()
{
	int c = INT_MAX;
	for (int i = t; i != s; i = pre[i])
		//if (R[pre[i]][i]<c)
		if (R[make_pair(pre[i],i)]<c)
			c = R[make_pair(pre[i],i)];
	for (int j = t; j != s; j = pre[j])
	{
		int i = pre[j];
		if (R[make_pair(j,i)]<0 && R[make_pair(j,i)] + c>0) e[j] = new edge(i, e[j]);
		if (i == s) ans += c;
		F[make_pair(i,j)] += c;
		F[make_pair(j,i)] -= c;
		R[make_pair(i,j)] -= c;
		R[make_pair(j,i)] += c;
	}
}

int max_flow(int sv, int tv) 
{
	//int n, m, i, x, y, w;
	//scanf("%d %d", &m, &n);
	//for (i = 0; i<m; i++)
	//{
	//	scanf("%d %d %d", &x, &y, &w);
	//	e[x] = new edge(y, e[x]);
	//	e[y] = new edge(x, e[y]);
	//	R[x][y] += w;
	//}
	s = sv;
	t = tv;
	while (Find_Augmenting_Path()) Augment();
	//printf("%d\n",ans);
	return ans;
}

void insert(int x, int y, int w) {
	e[x] = new edge(y, e[x]);
	e[y] = new edge(x, e[y]);
	R[make_pair(x,y)] += w;
	//cout << x << ' ' << y << ' ' << w << endl;
}

bool overlap(pair<int, int> x, pair<int, int> y) {
	if (x.first > x.second || y.first > y.second)
		return false;
	if (x.first <= y.first && y.first <= x.second)
		return true;
	if (x.first <= y.second && y.second <= x.second)
		return true;
	if (y.first <= x.first && x.first <= y.second)
		return true;
	if (y.first <= x.second && x.second <= y.second)
		return true;
	return false;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> T;
	for (int cse = 1; cse <= T; cse++) {
		ans = 0;
		memset(e, NULL, sizeof(e));
		//memset(F, 0, sizeof(F));
		F.clear();
		//memset(Q, 0, sizeof(Q));
		Q.clear();
		//memset(R, 0, sizeof(R));
		R.clear();
		//memset(pre, 0, sizeof(pre));
		pre.clear();
		//memset(visited, false, sizeof(visited));
		visited.clear();

		cin >> n >> p;
		r = vector<int>(n, 0);
		q = vector<vector<int>>(n, vector<int>(p, 0));
		v.clear();
		for (int i = 0; i < n; i++) {
			cin >> r[i];
		}
		for (int i = 0; i < n; i++) {
			vector<pair<int, int>> pv;
			for (int j = 0; j < p; j++) {
				cin >> q[i][j];
				int tmp = q[i][j];
				int ts = ceil(tmp/1.1/r[i]);
				int te = floor(tmp/0.9/r[i]);
				//cout << '[' << ts << ' ' << te << ']';
				pv.push_back(make_pair(ts, te));
			}
			v.push_back(pv);
		}

		//for (auto x : v) {
		//	for (auto y : x) {
		//		cout << '[' << y.first << ' ' << y.second << ']';
		//	}
		//	cout << endl;
		//}

		//0->1xx
		for (int i = 0; i < p; i++) {
			insert(0, 100 + i, 1);
		}
		//axx->a+1xx
		for (int i = 0; i < n; i++) {
			int x = ((i + 1) * 2 - 1) * 100;
			int y = ((i + 1) * 2) * 100;
			for (int j = 0; j < p; j++) {
				if (overlap(v[i][j], v[i][j]))
					insert(x + j, y + j, 1);
			}
		}
		//axx->bxx
		for (int l = 1; l < n; l++) {
			int lu = (l) * 200;
			int lv = ((l + 1) * 2 - 1) * 100;
			for (int i = 0; i < p; i++) {
				for (int j = 0; j < p; j++) {
					if (overlap(v[l - 1][i], v[l][j])) {
						int x = lu + i;
						int y = lv + j;
						int w = 1;
						insert(x, y, w);
					}
				}
			}
		}
		//nxx->t
		int t = (n * 2 + 1) * 100;
		int tx = (n * 2) * 100;
		for (int i = 0; i < p; i++) {
			insert(tx + i, t, 1);
		}

		int ans = max_flow(0, t);
		cout << "Case #" << cse << ": " << ans << endl;

	}
	return 0;
}


