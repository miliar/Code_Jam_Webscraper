#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;


int N, P;
int R[53];
vector<pair<int, int>> Q[53];

bool intersect(pair<int, int> a, pair<int, int> b) {
	if (a.second < b.first) return false;
	if (b.second < a.first) return false;
	return true;
}


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);

		FOR(t, 53) Q[t].clear();

		scanf("%d%d", &N, &P);
		FOR(i, N) scanf("%d", &R[i]);
		FOR(i, N) {
			FOR(zz, P) {
				int q; scanf("%d", &q);
				int lo = (q * 10 + R[i] * 11 - 1) / (R[i] * 11);
				int hi = (q * 10) / (R[i] * 9);
				if (lo > hi) continue;
				if (hi == 0) continue;
				Q[i].push_back(make_pair(lo, hi));
			}

			sort(Q[i].begin(), Q[i].end());
			reverse(Q[i].begin(), Q[i].end());
		}

		//puts("aaaaa");


		int ans = 0;
		while (true) {
			bool emptyExist = false;
			FOR(t, N) if (Q[t].empty()) emptyExist = true;
			if (emptyExist) break;

			pair<int, int> m = Q[0].back();
			int mi = 0;
			for (int t=1; t<N; t++) if (m > Q[t].back()) {
				m = Q[t].back();
				mi = t;
			}


			bool allIntersect = true;
			FOR(t, N) if (intersect(m, Q[t].back()) == false) {
				allIntersect = false;
				break;
			}

			if (allIntersect) {
				FOR(t, N) Q[t].pop_back();
				ans++;
			}
			else {
				Q[mi].pop_back();
			}
		}


		printf("%d\n", ans);





	}


	return 0;
}
