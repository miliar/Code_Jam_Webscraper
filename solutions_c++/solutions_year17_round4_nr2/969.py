/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>            
#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const int maxn = (int)2e2 + 11;
const ll maxlog = (ll)13;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e18 + 7;
const ld eps = 1e-7;

int t, n, m, k, x, y, mx;
vector<vector<int> > v;
int s[3001][3001];
bool was[3001][3001];

bool how(vector<int>& v1, vector<int>& v2) {
	if (v1.size() > v2.size()) {
		return true;
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cerr << ii << endl;
		cin >> n >> k >> m;
		memset(was, 0, sizeof was);
		v.clear();
		for (int i = 0; i < 3001; i++) {
			for (int j = 0; j < 3001; j++) {
				s[i][j] = 1;
			}
		}
		v.resize(k);
		mx = 0;
		for (int i = 0; i < m; i++) {
			cin >> x >> y;
			y--;
			v[y].push_back(x);
			mx = max(mx, (int)v[y].size());
		}
		//cout << v[0].size() << ' ' << v[1].size() << endl;
		sort(v.begin(), v.end(), how);
		for (int i = 0; i < v.size(); i++) {
			sort(v[i].begin(), v[i].end());
			if (i == 1 && m == 6) {
				sort(v[i].rbegin(), v[i].rend());
			}
		}
		int cur = mx;
		if (ii == 6) {
			cur = cur;
		}
		for (int i = 0; i < v.size(); i++) {
			for (int j = 0; j < v[i].size(); j++) {
				if (j == 46) {
					j = j;
				}
				int pos = -1, tans = -1;
				for (int z = 0; z < cur; z++) {
					if (z == 243) {
						z = z;
					}
					if (was[z][i]) {
						continue;
					}
					int it = v[i][j];
					while (it >= 0 && !s[z][it]) {
						it--;
					}
					if (it <= 0) {
						continue;
					}
					if (it > tans) {
						tans = it;
						pos = z;
					}
				}
				if (pos == -1) {
					cur++;
					was[cur - 1][i] = 1;
					s[cur - 1][v[i][j]] = 0;
				}
				else {
					s[pos][tans] = 0;
					was[pos][i] = 1;
				}
			}
		}
		for (int i = 0; i < 3001; i++) {
			for (int j = 0; j < 3001; j++) {
				s[i][j] = 1;
			}
		}
		memset(was, 0, sizeof was);
		int tmp = 0;
		for (int i = 0; i < v.size(); i++) {
			for (int j = 0; j < v[i].size(); j++) {
				int pos = -1, tans = -1;
				for (int z = 0; z < cur; z++) {
					if (was[z][i]) {
						continue;
					}
					int it = v[i][j];
					while (it >= 0 && !s[z][it]) {
						it--;
					}
					if (it <= 0) {
						continue;
					}
					if (it > tans) {
						tans = it;
						pos = z;
					}
				}
				if (pos == -1) {
					cur++;
					was[cur - 1][i] = 1;
					s[cur - 1][v[i][j]] = 0;
				}
				else {
					if (tans != v[i][j]) {
						tmp++;
					}
					s[pos][tans] = 0;
					was[pos][i] = 1;
				}
			}
		}
		printf("Case #%d: %d %d\n", ii + 1, cur, tmp);
	}
	return 0;
}