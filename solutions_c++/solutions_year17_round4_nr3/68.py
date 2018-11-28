#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define F(i,n) for(int i = 0; i < (n); i++)
#define FF(i,n) for(int i = 1; i <= (n); i++)
#define FE(i,n) for(int i = 0; i <= (n); i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const ll infl = 9012345678901234567;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//
const int MN = 2500;
class TwoSAT { //use even numbers for indices
public:
	int n;
	vector<int> adj[2 * MN];
	vector<int> rev_adj[2 * MN];
	int scc[2 * MN];
	int clk_order[2 * MN];
	int vis[2 * MN];
	int clock = 0;
	int sccnum;
	int truthval[2 * MN];
	//input of init: number of variables.
	void init(int _n) { n = _n << 1; for (int i = 0; i < n; i++) adj[i].clear(), rev_adj[i].clear(); }
	void addImplies(int a, int b) {
		adj[a].push_back(b);
		rev_adj[b].push_back(a);
		adj[b ^ 1].push_back(a ^ 1);
		rev_adj[a ^ 1].push_back(b ^ 1);
		//printf("ADD %d %d\n", a, b);
	}
	void dfs(int i) {
		vis[i] = 1;
		for (auto &x : rev_adj[i]) {
			if (vis[x]) continue;
			dfs(x);
		}
		clk_order[clock++] = i;
		return;
	}
	void dfs2(int i) {
		vis[i] = 1;
		scc[i] = sccnum;
		for (auto &x : adj[i]) {
			if (vis[x]) continue;
			dfs2(x);
		}
	}
	int check() {
		memset(vis, 0, sizeof(vis));
		clock = 0;
		for (int i = 0; i < n; i++) {
			if (vis[i]) continue;
			dfs(i);
		}
		memset(vis, 0, sizeof(vis));
		sccnum = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (vis[clk_order[i]]) continue;
			sccnum++;
			dfs2(clk_order[i]);
		}
		for (int i = 0; i < n; i += 2) {
			if (scc[i] == scc[i | 1]) return 0;
		}
		return 1;
	}
	void getTable() {
		for (int i = 0; i < n; i++) {
			truthval[i] = (scc[i] < scc[i ^ 1]);
		}
	}
}scc;

char b[51][51];
pair<int, int> dir[4] = { {0,1},{1,0},{0,-1},{-1,0} };
int main() {
#ifndef __GNUG__
	//freopen("input.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		int r, c; nii(r, c);
		F(i, r)scanf("%s", b[i]);
		scc.init(r*c);
		bool bad = false;
		F(i, r) {
			F(j, c) {
				int X = i*c + j;
				X = X << 1;
				if (b[i][j] == '|' || b[i][j] == '-' || b[i][j] == '.') {
					int ii, jj, di, dj, stat;
					int st2 = (b[i][j] == '.') ? 1 : 0; 
					vector<pair<pii,pii> > endp(4);
					vector<int> sts(4);
					F(k, 4) {
						ii = i, jj = j;
						di = dir[k].first, dj = dir[k].second;
						stat = 0;
						while (1) {
							ii += di;
							jj += dj;
							if (jj == -1 || ii == -1 || jj == c || ii == r)break;
							else if (ii == i&&jj == j) {
								stat = 2; break;
							}
							else if (b[ii][jj] == '.') {

							}
							else if (b[ii][jj] == '#')break;
							else if (b[ii][jj] == '|' || b[ii][jj] == '-') {
								stat = 1;
								break;
							}
							else if (b[ii][jj] == '/') {
								swap(di, dj);
								di = -di;
								dj = -dj;
							}
							else swap(di, dj);
						}
						sts[k] = stat;
						endp[k] = { {ii,jj}, {di,dj} };
						X = X ^ 1;
					}
					if (st2) {
						int k1 = -1, k2 = -1;
						if (sts[0] == 1) k1 = 0;
						else if (sts[2] == 1)k1 = 2;
						if (sts[1] == 1)k2 = 1;
						else if(sts[3] == 1)k2 = 3;
						if (k1 == -1 && k2 == -1)bad = true;
						else if (k1 == -1) {
							int ii = endp[k2].first.first;
							int jj = endp[k2].first.second;
							int Y = c*ii + jj;
							Y <<= 1;
							if (endp[k2].second.first)Y++;
							scc.addImplies(Y ^ 1, Y);
						}
						else if (k2 == -1) {

							int ii = endp[k1].first.first;
							int jj = endp[k1].first.second;
							int Y = c*ii + jj;
							Y <<= 1;
							if (endp[k1].second.first)Y++;
							scc.addImplies(Y ^ 1, Y);
						}
						else {
							int Y1 = c*endp[k1].first.first + endp[k1].first.second;
							int Y2 = c*endp[k2].first.first + endp[k2].first.second;
							Y1 *= 2;
							Y2 *= 2;
							if (endp[k1].second.first)Y1++;
							if (endp[k2].second.first)Y2++;
							scc.addImplies(Y1 ^ 1, Y2);
						}
					}
					else {
						F(k, 4) {
							if (sts[k]) {
								scc.addImplies(X, X ^ 1);
							}
							X ^= 1;
						}
					}
				}
			}
		}

		if (bad || !scc.check()) {
			puts("IMPOSSIBLE");
		}
		else {
			puts("POSSIBLE");
			scc.getTable();
			F(i, r)F(j, c) {
				if (b[i][j] != '-' && b[i][j] != '|')continue;
				int X = i*c + j;
				if (scc.truthval[X << 1]) {
					b[i][j] = '-';
				}
				else b[i][j] = '|';
			}
			F(i, r)printf("%s\n", b[i]);
		}
		fprintf(stderr, "Case %d complete\n", casen);
	}
	return 0;
}