#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

int r, c;
vector<string> v;
vector<pair<int, int>> g;

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int q = 0; q < T; q++) {
		cin >> r >> c;
		v.resize(r);
		g.clear();
		for (int i = 0; i < r; i++) {
			cin >> v[i];
			for (int j = 0; j < c; j++) {
				if (v[i][j] != '?') {
					g.push_back(mp(i, j));
				}
			}
		}
		set<int> S;
		for (auto el : g) S.insert(el.first);
		int last = 0;
		auto el = S.begin();
		while (el != S.end()) {
			auto nxt = el;
			++nxt;
			int nxtrow = r;
			if (nxt != S.end()) {
				nxtrow = *nxt;
			}
			vector<pair<int, int>> u;
			for (auto l : g) {
				if (l.first == *el) {
					u.push_back(l);
				}
			}
			sort(u.begin(), u.end());
			set<int> G;
			for (auto l : u) G.insert(l.second);
			auto gel = G.begin();
			int lastlast = 0;
			int hh = 0;
			while (gel != G.end()) {
				auto gxt = gel;
				gxt++;
				int nxtcol = c;
				if (gxt != G.end()) {
					nxtcol = *gxt;
				}
				char c = v[u[hh].first][u[hh].second];
				for (int i = last; i < nxtrow; i++) {
					for (int j = lastlast; j < nxtcol; j++) {
						v[i][j] = c;
					}
				}
				lastlast = nxtcol;
				gel++;
				hh++;
			}
			last = nxtrow;
			el++;
		}
		printf("Case #%d:\n", q + 1);
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) cout << v[i][j];
			cout << "\n";
		}
	}

	return 0;
}