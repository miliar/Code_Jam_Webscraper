#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> llp;

const ll INF = 1000000000000;

struct tr {
	ld time;
	ll pos;
	bitset<100> used;
};

bool operator<(tr lhs, tr rhs) {
	if (lhs.time < rhs.time) { return true; }
	return false;
}

int main() {
	ll t;
	cin >> t;

	for (ll q = 0; q < t; q++) {
		ll n, p;
		cin >> n >> p;

		vector<ll> d[100];
		vector<llp> hs(n);

		for (ll i = 0; i < n; i++) {
			d[i].resize(n);
		}

		for (ll i = 0; i < n; i++) {
			cin >> hs[i].first >> hs[i].second;
		}

		for (ll i = 0; i < n; i++) {
			for (ll j = 0; j < n; j++) {
				cin >> d[i][j];
			}
		}

		for (ll k = 0; k < n; k++) {
			for (ll i = 0; i < n; i++) {
				for (ll j = 0; j < n; j++) {
					if (d[i][k] != -1 && d[k][j] != -1 && (d[i][k] + d[k][j] < d[i][j] || d[i][j] == -1)) {
						d[i][j] = d[i][k] + d[k][j];
					}
				}
			}
		}

		cout << "Case #" << q + 1 << ": ";

		for (ll w = 0; w < p; w++) {
			ll u, v;
			cin >> u >> v;
			u--; v--;

			vector<ld> mint(n, INF);
			mint[u] = 0;
			bitset<100> sused = 0;
			sused.set(u);

			set<tr> st;
			tr start;
			start.used = sused;
			start.pos = u;
			start.time = 0;
			st.insert(start);

			while (!st.empty()) {
				tr cur = *st.begin();
				st.erase(st.begin());

				if (cur.pos == v) {
					cout << setprecision(8) << fixed << cur.time << " ";
					break;
				}

				if (cur.time > mint[cur.pos]) {
					continue;
				}

				cur.used.set(cur.pos);
				bitset<100> nused = cur.used;

				for (ll i = cur.pos+1; i < n; i++) {
					if (!cur.used[i] && d[cur.pos][i] <= hs[cur.pos].first) {
						tr nw;
						nw.used = nused;
						nw.time = ld(cur.time) + d[cur.pos][i] / ld(hs[cur.pos].second);
						nw.pos = i;
						if (nw.time < mint[i]) {
							st.insert(nw);
							mint[i] = nw.time;
						}
					}
				}
			}
		}
		cout << "\n";
	}

	return 0;
}