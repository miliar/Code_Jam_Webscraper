// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;

const int N = (int) 1e5 + 5, mod = (int) 0;
string mat[N];
set<int> all[N];
vector<int> in[N], out[N];
int t, res[N], tp[N], col[N], mark[N];
void add_edge(int u, int v) {
	out[u].push_back(v);	
	in[v].push_back(u);
}
void add_clause(int u, int v) {
	add_edge(u ^ 1, v);
	add_edge(v ^ 1, u);
}
void dfs(int v) {
	if (mark[v]++) return;
	for (int u : out[v]) {
		dfs(u);
	}
	tp[t++] = v;
}
void sfd(int v, int c) {
	if (mark[v]++) return;
	col[v] = c;
	for (int u : in[v]) {
		sfd(u, c);
	}
}
bool two_sat(int n) {
	for (int j = 0; j < n; ++j) mark[j] = 0;
	t = 0;
	for (int j = 0; j < n; ++j)
		if (!mark[j])
			dfs(j);
	int cc = 0;
	for (int j = 0; j < n; ++j) mark[j] = 0;
	for (int _ = t - 1; _ >= 0; --_) {
		int v = tp[_];
		if (!mark[v]) {
			sfd(v, cc++);	
		}
	}
	for (int j = 0; j < n; ++j) {
		if (col[j] == col[j ^ 1]) {
			return 0;
		}
		res[j] = (col[j] > col[j ^ 1]);
	}
	return 1;
}
int n, m;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
bool beam(int x, int y) { return mat[x][y] == '-' || mat[x][y] == '|';	}
int f(int i, int j) {
	return i * m + j;		
}
int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		cin >> n >> m;
		for (int j = 0; j < 2 * n * m + 10; ++j) {
			all[j].clear();
			out[j].clear();
			in[j].clear();
		}
		for (int j = 0; j < n; ++j) {
			cin >> mat[j];
		}
		for (int x = 0; x < n; ++x)
			for (int y = 0; y < m; ++y) {
				if (beam(x, y)) {
					for (int way = 0; way <= 1; ++way) {
						vector<int> see;
						int flag = 0;
						int cur = f(x, y) << 1 | way;
						for (int stdir = 0; stdir <= 1; ++stdir) {
							int cnt = 0;
							int dir = way;
							if (stdir) dir = 3 ^ dir;
							int curx = x, cury = y;
							while (cnt < n * m + 10 && curx >= 0 && curx < n && cury >= 0 && cury < m) {
								if (mat[curx][cury] == '#') {
									break;	
								}
								see.push_back(f(curx, cury));
								if (beam(curx, cury) && cnt != 0) {
									flag = 1;
									break;
								}
								if (mat[curx][cury] == '/') {
									dir ^= 2;
								} else {
									if (mat[curx][cury] != '.' && !beam(curx, cury) && mat[curx][cury] != '#') {
										dir ^= 1;	
									}	
								}
		//						cout << cnt << ' ' << curx << ' ' << cury << ' ' << dir << endl;
								curx += dx[dir];
								cury += dy[dir];
								++cnt;
							}
						}

						if (flag) {
							add_edge(cur, cur ^ 1);	
						} else {
							for (int p : see) all[p].insert(cur);
						}
					}
				}
			}
		int noway = 0;
		for (int ind = 0; ind < n * m; ++ind) {
			int x = ind / m, y = ind % m;
			if (mat[x][y] != '.') continue;
			if (all[ind].size() > 2) {
				assert(0);
			}
			if (all[ind].size() == 0) {
				noway = 1;	
				break;
			}
//			cout << " : ) " << ind << ' ' << all[ind].size() << endl;
			auto it = all[ind].begin();
			if (all[ind].size() == 1) {
				add_edge((*it) ^ 1, (*it));
			} else {
				auto nx = it; ++nx;
//				cout << " hmmm " << ind << ' ' << (*nx) << ' ' << (*it) << endl;
				add_clause(*nx, *it);
			}
		}
		if (noway) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		if (two_sat(n * m * 2)) {
			cout << "POSSIBLE\n";	
			for (int x = 0; x < n; ++x) {
				for (int y = 0; y < m; ++y) {
					if (!beam(x, y)) {
						cout << mat[x][y];
					} else {
						cout << (res[f(x, y) << 1] == 1 ? '|' : '-');
					}
				}
				cout << '\n';
			}
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}
}

















