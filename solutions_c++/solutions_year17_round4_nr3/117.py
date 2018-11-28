#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

int r, c;
char g[50][50];
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
int rfwd[4] = { 3, 2, 1, 0 };
int rbck[4] = { 2, 3, 0, 1 };
vector<pair<int,char>> cover[50][50];
vector<pair<int,int>> lazer;

bool shoot(int l, char z, int x, int y, int d) {
	x += dx[d];
	y += dy[d];
	if (x < 0 || x >= r || y < 0 || y >= c) {
		return false;
	} else if (g[x][y] == '|' || g[x][y] == '-') {
		return true;
	} else if (g[x][y] == '/') {
		return shoot(l, z, x, y, rfwd[d]);
	} else if (g[x][y] == '\\') {
		return shoot(l, z, x, y, rbck[d]);
	} else if (g[x][y] == '#') {
		return false;
	}
	cover[x][y].push_back(make_pair(l, z));
	return shoot(l, z, x, y, d);
}

bool recurse(char g[50][50]) {
	FOR(x, r) {
		FOR(y, c) {
			if (g[x][y] == '.') {
				FORVEC(ii, cover[x][y]) {
					int lx = lazer[ii->first].first;
					int ly = lazer[ii->first].second;
					if (g[lx][ly] == ii->second) {
						g[x][y] = 'x';
						break;
					}
				}
				if (g[x][y] == 'x') continue;
				vector<pair<int,char>> candidates;
				FORVEC(ii, cover[x][y]) {
					int lx = lazer[ii->first].first;
					int ly = lazer[ii->first].second;
					if (g[lx][ly] == '?') {
						candidates.push_back(*ii);
					}
				}
				if (candidates.size() == 0) return true;
				if (candidates.size() == 1) {
					int lx = lazer[candidates[0].first].first;
					int ly = lazer[candidates[0].first].second;
					g[lx][ly] = candidates[0].second;
					g[x][y] = 'x';
					continue;
				}
				FORVEC(jj, candidates) {
					int lx = lazer[jj->first].first;
					int ly = lazer[jj->first].second;
					g[lx][ly] = jj->second;
					g[x][y] = 'x';
					char k[50][50];
					FOR(i,r) FOR(j,c) k[i][j] = g[i][j];
					//cout << "Trying to set " << lx << " / " << ly << " to " << jj->second << endl;
					if (!recurse(k)) {
						//cout << "Yes" << endl;
						FOR(i,r) FOR(j,c) g[i][j] = k[i][j];
						return false;
					}
					//cout << "Nope" << endl;
					g[lx][ly] = '?';
				}
				return true;
			}
		}
	}
	return false;
}

bool solve()
{
	cin >> r >> c;
	lazer.clear();
	FOR(x, r) {
		FOR(y, c) {
			cin >> g[x][y];
			cover[x][y].clear();
		}
	}
	FOR(x, r) {
		FOR(y, c) {
			if (g[x][y] == '|' || g[x][y] == '-') {
				int lnum = lazer.size();
				lazer.push_back(make_pair(x, y));
				bool destroys_y = shoot(lnum, '-', x, y, 0) || shoot(lnum, '-', x, y, 1);
				bool destroys_x = shoot(lnum, '|', x, y, 2) || shoot(lnum, '|', x, y, 3);
				if (destroys_y && destroys_x) return true;
				if (destroys_x) {
					g[x][y] = '-';
				} else if (destroys_y) {
					g[x][y] = '|';
				} else {
					g[x][y] = '?';
				}
			}
		}
	}
	if (recurse(g)) {
		return true;
	}
	cout << "POSSIBLE" << endl;
	FOR(x, r) {
		FOR(y, c) {
			cout << (g[x][y] == 'x' ? '.' : (g[x][y] == '?' ? '-' : g[x][y]));
		}
		cout << endl;
	}
	return false;
}

int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		bool imp = solve();
		if (imp) {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
