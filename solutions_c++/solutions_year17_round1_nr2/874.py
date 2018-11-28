#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

typedef long long ll;

const int MAX_N = 50, MAX_P = 50;

int T, N, P, Rl[MAX_N], Rh[MAX_N], Q[MAX_N][MAX_P], Ql[MAX_N][MAX_P], Qh[MAX_N][MAX_P], ptr[MAX_N];

bool in_range(int i1, int j1, int i2, int j2) {
	return Qh[i1][j1] >= Ql[i2][j2] && Ql[i1][j1] <= Qh[i2][j2];
}

bool less_than(int i1, int j1, int i2, int j2) {
	return Ql[i1][j1] < Ql[i2][j2] || Qh[i1][j1] < Qh[i2][j2];
}

int main() {
	// freopen("B-small-attempt0.in", "r", stdin);
	// freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("r1a_b.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		scanf("%d %d", &N, &P);
		
		FOR(i, 0, N) {
			int r;
			scanf("%d", &r);
			
			Rl[i] = r * 9;
			Rh[i] = r * 11;
		}
		
		FOR(i, 0, N) {
			FOR(j, 0, P) {
				scanf("%d", &Q[i][j]);
			}
		}
		FOR(i, 0, N) {
			sort(Q[i], Q[i] + P);
			FOR(j, 0, P) {
				Ql[i][j] = 1 + (Q[i][j] * 10 - 1) / Rh[i];
				Qh[i][j] = Q[i][j] * 10 / Rl[i];
				// printf("hi %d %d\n", Ql[i][j], Qh[i][j]);
			}
		}
		
		int result = 0;
		
		FOR(i, 0, N) {
			ptr[i] = 0;
		}
		FOR(j0, 0, P) {
			bool mismatched = false;
			ptr[0] = j0 + 1;
			
			if (Ql[0][j0] > Qh[0][j0]) continue;
			
			// printf("j0 = %d\n", j0);
			
			FOR(i, 1, N) {
				// printf("i = %d\n", i);
				while (true) {
					if (ptr[i] >= P) {
						mismatched = true;
						break;
					}
					if (Ql[i][ptr[i]] > Qh[i][ptr[i]]) {
						ptr[i]++;
					}
					else {
						if (in_range(i - 1, ptr[i - 1] - 1, i, ptr[i])) {
							ptr[i]++;
							break;
						}
						else {
							if (less_than(i, ptr[i], i - 1, ptr[i - 1] - 1)) {
								ptr[i]++;
							}
							else {
								// printf("mismatched = true;\n", i);
								mismatched = true;
								ptr[i] = 0;
								break;
							}
						}
					}
				}
				if (mismatched) break;
			}
			
			if (!mismatched) {
				result++;
			}
		}

		printf("Case #%d: ", t);
		printf("%d", result);
		printf("\n");
	}
	return 0;
}
