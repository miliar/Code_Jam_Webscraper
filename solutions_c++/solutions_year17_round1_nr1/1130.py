#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <utility>
#include <vector>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define PI 3.14159265
#define INF 1023123123
#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c; --a)

using namespace std;

int main() {
	int R, C, T;
	char st[50], grid[30][30];
	pair <int, int> child[650];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		int cnt = 0;
		vector <int> row[30], col[30], allCol;
		bool flag[30];

		scanf("%d %d", &R, &C);

		memset(flag, false, sizeof(flag));

		FORU(r, 1, R) {
			scanf("%s", st);

			FORU(c, 1, C) {
				grid[r][c] = st[c - 1];

				if (grid[r][c] != '?') {
					child[cnt++] = mp(c, r);
					row[r].pb(c);
					col[c].pb(r);

					if (!flag[c]) {
						flag[c] = true;
						allCol.pb(c);
					}
				}
			}
		}

		FORU(r, 1, R) {
			if (!row[r].empty()) {
				sort(row[r].begin(), row[r].end());
			}
		}

		FORU(c, 1, C) {
			if (!col[c].empty()) {
				sort(col[c].begin(), col[c].end());
			}
		}

		sort(child, child + cnt);
		sort(allCol.begin(), allCol.end());

		for (int i = 0; i < cnt; ++i) {
			int atas = 1, bawah = R, kiri = 1, kanan = C;
			char replacement = grid[child[i].se][child[i].fi];

			if (i > 0) {
				if (child[i - 1].fi == child[i].fi) {
					atas = child[i - 1].se + 1;
				}

				int idx = lower_bound(allCol.begin(), allCol.end(), child[i].fi) - allCol.begin();

				if (idx != 0)
					kiri = allCol[idx - 1] + 1;
			}

			if (i < cnt - 1) {
				if (child[i + 1].fi == child[i].fi) {
					bawah = child[i].se;
				}

				int idx = lower_bound(allCol.begin(), allCol.end(), child[i].fi + 1) - allCol.begin();

				if (idx != allCol.size()) {
					kanan = child[i].fi;
				}
			}

			FORU(r, atas, bawah) {
				FORU(c, kiri, kanan) {
					grid[r][c] = replacement;
				}
			}
		}

		printf("Case #%d:\n", tc);

		FORU(r, 1, R) {
			FORU(c, 1, C)
				printf("%c", grid[r][c]);

			printf("\n");
		}
	}

	return 0;
}