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
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>
//#include "sort.h"

#define ll long long
#define ld double
#define pii pair <int, int>
#define pll pair <ll, ll>
#define mp make_pair

using namespace std;

const int maxn = 110;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;

	cin >> t;

	for (int ttt = 1; ttt <= t; ttt++) {
		printf("Case #%d: ", ttt);

		int hd, ad, hk, ak, b, d;

		cin >> hd >> ad >> hk >> ak >> b >> d;

		if (ad >= hk) {
			cout << 1 << endl;
			continue;
		}

		if (ak >= hd) {
			//cout << "IMPOSSIBLE" << endl;
			//continue;
		}

		int ans = (int)1e9;

		for (int i = 0; i <= 100; i++) {
			int cnt = 0;
			int h = hd;
			int a = ak;

			for (int j = 0; j < i; ) {
				cnt++;
				if (h <= max(0, a - d)) {
					h = hd - a;
				} else {
					a = max(0, a - d);
					h -= a;
					j++;
				}

				if (cnt > 300) {
					break;
				}
			}

			if (cnt > 300) {
				continue;
			}

			int hhh = h;
			int cntt = cnt;

			for (int k = 0; k <= 100; k++) {
				h = hhh;
				cnt = cntt;
				int o = ad;

				for (int j = 0; j < k; ) {
					cnt++;
					if (h <= a) {
						h = hd - a;
					} else {
						h -= a;
						o += b;
						j++;
					}

					if (cnt >= 600) {
						break;
					}
				}

				if (cnt >= 600) {
					continue;
				}

				int hh = hk;

				while (hh > 0) {
					cnt++;

					if (cnt >= 900) {
						break;
					}

					if (hh <= o) {
						break;
					}

					if (h <= a) {
						h = hd - a;
						continue;
					}

					hh -= o;
					h -= a;
				}

				if (cnt >= 900) {
					continue;
				}

				ans = min(ans, cnt);
			}
		}

		if (ans != (int)1e9) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}
