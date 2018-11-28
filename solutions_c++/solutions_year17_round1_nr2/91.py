#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

int T, R, C, n[55], cur[55], tmp[55][55];
pair<int, int> g[55][55];

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		fo(i, 0, 55) n[i] = 0, cur[i] = 0;
		fo(i, 0, 55) fo(j, 0, 55) tmp[i][j] = 0;
		fo(i, 0, 55) fo(j, 0, 55) g[i][j] = {0, 0};
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);

		scanf("%d %d", &C, &R);
		fo(i, 0, C) scanf("%d", &n[i]);
		fo(i, 0, C) {
			fo(j, 0, R) scanf("%d", &tmp[i][j]);
			sort(tmp[i], tmp[i] + R);
		}

		fo(i, 0, R) fo(j, 0, C) {
			int x = tmp[j][i];
			int l = (x * 10 + 10) / 11, r = x * 10 / 9;

			int a = (l + n[j] - 1) / n[j];
			int b = r / n[j];

			assert(a * n[j] >= l);
			assert(b * n[j] <= r);
			assert((a-1) * n[j] < l);
			assert((b+1) * n[j] > r);

			if (a > b) g[i][j] = MP(-1, -1);
			else g[i][j] = MP(a, b);
		}

		fo(j, 1, C) {
			while (cur[j] < R && g[cur[j]][j].first == -1) {
				cur[j]++;
			}
		}

		int ans = 0;
		fo(i, 0, R) if (g[i][0].first != -1) {
			int x = g[i][0].first, y = g[i][0].second, ok = 1;
			fo(j, 1, C) {
				while (cur[j] < R && g[cur[j]][j].second < x) cur[j]++;
				if (cur[j] == R) {
					ok = 0;
					break;
				}
				x = max(x, g[cur[j]][j].first);
				y = min(y, g[cur[j]][j].second);
			}
			if (ok && x <= y) {
				//printf("%d %d, %d %d\n", g[0][0].first, g[0][0].second, g[0][1].first, g[0][1].second);
				//asdf("%d %d\n", x, y);
				ans++;
				fo(j, 1, C) cur[j]++;
			}
		}

		printf("Case #%d: %d\n", t, ans);
		asdf("%d\n", ans);
	}
	return 0;
}
