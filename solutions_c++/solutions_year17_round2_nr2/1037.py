#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

const int MAXN = 1005;
int ans[3][MAXN];
char colors1[3] = { 'R', 'Y', 'B' };

int main() {
	int T;
	scanf("%d", &T);
	FOR(tc, 1, T) {
		int N, C1[3], C2[3];
		scanf("%d%d%d%d%d%d%d", &N, &C1[0], &C2[2], &C1[1], &C2[0], &C1[2], &C2[1]);
		assert(C2[0] == 0 && C2[1] == 0 && C2[2] == 0);

		int ansk = -1;
		REP(k, 3) {
			int CC1[3], CC2[3];
			REP(i, 3) CC1[i] = C1[i];
			REP(i, 3) CC2[i] = C2[i];
			bool possible = true;
			REP(i, N) {
				int best = -1;
				REP(j, 3) {
					if (CC1[j] == 0) continue;
					if (i == 0 && j != k) continue;
					if (i == N-1 && j == k) continue;
					if (i != 0 && j == ans[k][i-1]) continue;
					if (best == -1 || CC1[j] > CC1[best]) best = j;
				}
				if (best == -1) {
					possible = false;
					break;
				}
				ans[k][i] = best;
				CC1[best]--;
			}
			if (possible) {
				ansk = k;
				break;
			}
		}

		printf("Case #%d: ", tc);
		if (ansk != -1) {
			REP(i, N) printf("%c", colors1[ans[ansk][i]]);
		} else {
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}
	return 0;
}
