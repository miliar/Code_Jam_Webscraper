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

int n, p;
vector<ll> g;
vector<map<int, int>> M;

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int q = 0; q < T; q++) {
		cin >> n >> p;
		g.resize(n);
		for (int i = 0; i < n; i++) {
			cin >> g[i];
		}
		M.assign(n, map<int, int>());
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				int t;
				cin >> t;
				M[i][t]++;
			}
		}
		int ans = 0;
		ll x = 1;
		while (1) {
			for (int i = 0; i < n; i++) {
				if (M[i].empty()) {
					goto finish;
				}
				auto it = M[i].begin();
				if (it->second <= 0) {
					M[i].erase(M[i].begin());
					i--;
					continue;
				}
				ll mx = x * g[i] * 110;
				ll mn = x * g[i] * 90;
				if (mx >= it->first * 100 && mn <= it->first * 100) {
					continue;
				}
				else {
					if (mn > it->first * 90) {
						M[i].erase(it);
						i--;
						continue;
					}
					else {
						goto nxtstep;
					}
				}
			}
			for (int i = 0; i < n; i++) {
				auto it = M[i].begin();
				M[i][it->first]--;
			}
			ans++;
			if (false) {
			nxtstep:;
				x++;
			}
		}
	finish:;
		printf("Case #%d: ", q + 1);
		printf("%d\n", ans);
	}

	return 0;
}