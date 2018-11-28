#include <cinttypes>
#include <inttypes.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>
#include <string.h>
#include <list>
#include <queue>
#include <bitset>
#include <functional>

#define vi vector<int>
#define vvi vector<vi>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long

#define all(s) s.begin(), s.end()

using namespace std;

int nxi() { int a; cin >> a; return a; }

vector<ll> a;
void inc(int i, ll v) {
	for (; i < a.size(); i |= i + 1) {
		a[i] = max(a[i], v);
	}
}

long long get(int r) {
	long long ans = 0;
	for (; r >= 0; r = (r & (r + 1)) - 1) {
		ans = max(ans, a[r]);
	}
	return ans;
}

long long get(int l, int r) {
	return get(r) - get(l - 1);
}


int gcd(int a, int b) { return a == 0 ? b : gcd(b % a, a); }

bool cmp(pii a, pii b) {
	return a > b;
}

int main() {

	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

int TCount = nxi();
for (int T = 1; T <= TCount; ++T) {

	int n = nxi(), q = nxi();

	vpii horses(n);
	vvi adj(n, vi(n, -1));

	for (int i = 0; i < n; ++i) {
		cin >> horses[i].first >> horses[i].second;
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> adj[i][j];
		}
	}

	vector<vector<double>> times(n, vector<double>(n, 1e+16));

	for (int h = 0; h < n; ++h) {
		queue<pii> q;
		times[h][h] = 0;

		q.push(pii(h, horses[h].first));

		while (!q.empty()) {
			auto cur = q.front(); q.pop();

			for (int v = 0;v < n; ++v) {
				if (adj[cur.first][v] != -1 && cur.second >= adj[cur.first][v]) {
					double time = double(adj[cur.first][v]) / horses[h].second;
					if (times[h][v] > times[h][cur.first] + time) {
						times[h][v] = times[h][cur.first] + time;
						q.push(pii(v, cur.second - adj[cur.first][v]));
					}
				}

			}
		}
	}


	printf("Case #%d: ", T);

	for (int h = 0; h < q; ++h) {
		int u = nxi(), v = nxi();
		u--, v--;

		vi inq(n, 0);
		vector<double> d(n, 1e+16);
		d[u] = 0;
		queue<int> q;
		q.push(u);
		while (!q.empty()) {
			int cur = q.front(); q.pop();
			inq[cur] = 0;

			for (int v = 0; v < n; ++v) {
				if (d[v] > d[cur] + times[cur][v] ) {
					d[v] = d[cur] + times[cur][v];
					if (!inq[v]) {
						inq[v] = 1;
						q.push(v);
					}
				}
			}
		}


		printf("%.8f ", d[v]);
	}

	cout << endl;
	



}

	return 0;
}

