#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <stdio.h>
#include <set>
#include <algorithm>
#include <string.h>
#include <sstream>
#include <assert.h>
#include <time.h>
#include <string>
#include <queue>
#include <random> 
#include <map>
#include <numeric>
using namespace std;
typedef long long li;
#define mp make_pair
#define sz(a) (int)a.size()
const int N = 1e3 + 5;
const int K = 1e4 + 5;
const int INF = 1e9 + 7;
int n, k;
vector<int> g[N];
vector<int> mt;
vector<char> used;

bool try_kuhn(int v) {
	if (used[v])  return false;
	used[v] = true;
	for (size_t i = 0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (mt[to] == -1 || try_kuhn(mt[to])) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}


void solve() {
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		int nn, c, m;
		cin >> nn >> c >> m;

		for (int i = 0; i < N; i++) {
			g[i].clear();
		}
		vector<int> gg[3];
		for (int i = 0; i < m; i++) {
			int place, idx;
			cin >> place >> idx;
			gg[idx].push_back(place);
		}

		n = gg[1].size();
		k = gg[2].size();
		for (int i = 0; i < gg[1].size(); i++) {
			for (int j = 0; j < gg[2].size(); j++) {
				if (gg[1][i] != gg[2][j]) {
					g[i].push_back(j);
				}
			}
		}
		mt.assign(k, -1);
		for (int v = 0; v < n; ++v) {
			used.assign(n, false);
			try_kuhn(v);
		}
		int ans1 = 0;
		for (int i = 0; i < k; ++i) {
			if (mt[i] != -1) {
				ans1++;
			}
		}

		for (int i = 0; i < gg[1].size(); i++) {
			for (int j = 0; j < gg[2].size(); j++) {
				if (gg[1][i] != 1 || gg[2][j] != 1) {
					g[i].push_back(j);
				}
			}
		}
		mt.assign(k, -1);
		for (int v = 0; v < n; ++v) {
			used.assign(n, false);
			try_kuhn(v);
		}

		int ans2 = 0;
		for (int i = 0; i < k; ++i) {
			if (mt[i] != -1) {
				ans2++;
			}
		}


		int o1 = n - ans2;
		int o2 = k - ans2;

		int answer1 = ans2 + o1 + o2;
		int answer2 = ans2 - ans1;

		cout << "Case #" << test + 1 << ": " << answer1 << " " << answer2 << endl;
	}
}

int main() {
#ifdef _DEBUG
#endif
	freopen("B-small-attempt1 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cout.sync_with_stdio(false);
	cin.tie(0);
	srand(time(NULL));
	solve();
	return 0;
}