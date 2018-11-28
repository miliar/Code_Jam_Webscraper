#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int N, P;
		scanf("%d%d", &N, &P);
		int g[4] = { 0 };
		for (int i = 0; i < N; i++) {
			int a;
			scanf("%d", &a);
			g[a%P]++;
		}
		int ans = 0;
		if (P == 2) {
			ans = g[0];
			ans += g[1] / 2;
			ans++;
			if (g[1] % 2 == 0) {
				ans--;
			}
		} else if (P == 3) {
			ans = g[0];
			int pair = min(g[1], g[2]);
			ans += pair;
			ans += (g[1] + g[2] - pair * 2) / 3;
			ans++;
			if ((g[1] + g[2] - pair * 2) % 3 == 0) {
				ans--;
			}
		} else if (P == 4) {
			ans = g[0];
			int pair = min(g[1], g[3]);
			ans += pair;
			g[1] -= pair;
			g[3] -= pair;
			pair = g[2] / 2;
			ans += pair;
			g[2] -= pair * 2;
			if (g[2] == 1) {
				if (g[1] >= 2) {
					ans++;
					g[1] -= 2;
					g[2]--;
				} else if (g[3] >= 2) {
					ans++;
					g[3] -= 2;
					g[2]--;
				}
			}
			ans += g[1] / 4;
			g[1] %= 4;
			ans += g[3] / 4;
			g[3] %= 4;

			if (g[1] > 0 || g[2] > 0 || g[3] > 0) {
				ans++;
			}
		}


		/*
		int pack = (sum - 1) / P + 1;
		int yoyuu = pack * P - sum;
		vector<int> amari;
		int r = 0;
		for (int i = 0; i < N; i++) {
			amari.push_back(r);
			r += g[i];
			r %= P;
		}
		int cnt[100][4] = {0};
		for (int i = 0; i < N; i++) {
			if (i > 0) {
				for (int j = 0; j < 4; j++) {
					cnt[i][j] = cnt[i - 1][j];
				}
			}
			cnt[i][amari[i]]++;
		}
		int ans = 0;
		if (yoyuu <= 0) {
			ans = cnt[N-1][0];
		} else {
			for (int i = 0; i < N; i++) {
				if (yoyuu <= 1) {
					ans = max(ans, cnt[i][0] + cnt[N - 1][1] - cnt[i][1]);
				} else {
					for (int j = i; j < N; j++) {
						if (yoyuu <= 2) {
							ans = max(ans, cnt[i][0] + cnt[j][1] - cnt[i][1] + cnt[N-1][2] - cnt[j][2]);
						} else {
							for (int k = j; k < N; k++) {
								ans = max(ans, cnt[i][0] + cnt[j][1] - cnt[i][1] + cnt[k][2] - cnt[j][2] + cnt[N-1][3] - cnt[k][3]);
							}
						}
					}
				}
			}
		}
		*/
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
