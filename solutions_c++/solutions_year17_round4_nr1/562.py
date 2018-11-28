#include <bits/stdc++.h>

using namespace std;

int groupz[111];
int F[2][111][111][111];
int when[2][111][111][111];

inline void update(int i, int r1, int r2, int r3, int v)
{
	int ti = i & 1;
	int oi = ti ^ 1;
	if (when[oi][r1][r2][r3] != i + 1) {
		when[oi][r1][r2][r3] = i + 1;
		F[oi][r1][r2][r3] = v;
	} else {
		F[oi][r1][r2][r3] = max(F[oi][r1][r2][r3], v);
	}
	// printf("F[%d][%d][%d][%d] = %d\n", i + 1, r1, r2, r3, v);
}

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++TK);
		fprintf(stderr, "Case #%d\n", TK);

		int N, P;
		scanf("%d %d", &N, &P);
		for (int i = 0; i < N; i++) {
			scanf("%d", &groupz[i]);
		}
		memset(F, 0, sizeof(F));
		memset(when, -1, sizeof(when));
		when[0][0][0][0] = 0;
		for (int i = 0; i < N; i++) {
			int ti = i & 1;
			int r[4] = {0};
			for (r[1] = 0; r[1] <= N; r[1]++) {
				for (r[2] = 0; r[2] <= N; r[2]++) {
					for (r[3] = 0; r[3] <= N; r[3]++) {
						if (when[ti][r[1]][r[2]][r[3]] != i) continue;

						int remain = groupz[i] % P;
						int v = F[ti][r[1]][r[2]][r[3]];
						// fprintf(stderr, "base ");
						update(i, r[1] + (remain == 1), r[2] + (remain == 2), r[3] + (remain == 3), v + 1);
						for (int j = 1;j < P;j++) {
							if (r[j] <= 0) continue;
							int nj = (j + remain) % P;
							// fprintf(stderr, "j = %d, F[%d][%d][%d][%d] -> ", j, i, r[1], r[2], r[3]);
							r[nj]++;
							r[j]--;
							update(i, r[1], r[2], r[3], v);
							r[j]++;
							r[nj]--;
						}
					}
				}
			}
		}
		int ans = 0;
		if (when[N&1][0][0][0] == N) ans = max(ans, F[N&1][0][0][0]);
		if (when[N&1][1][0][0] == N) ans = max(ans, F[N&1][1][0][0]);
		if (when[N&1][0][1][0] == N) ans = max(ans, F[N&1][0][1][0]);
		if (when[N&1][0][0][1] == N) ans = max(ans, F[N&1][0][0][1]);
		printf("%d\n", ans);
	}
	return 0;
}
