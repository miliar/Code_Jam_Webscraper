#include <algorithm>
#include <cassert>
#include <cstdio>
#include <vector>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

int ceildiv(int a, int b) { return (a + b - 1) / b; }

int main() {
	int T;
	scanf("%d", &T);
	FOR(tc, 1, T) {
		int N, P;
		scanf("%d%d", &N, &P);
		vector<int> C(P);
		REP(i, N) {
			int G;
			scanf("%d", &G);
			C[G % P]++;
		}
		int ans = C[0];
		if (P == 2) {
			ans += ceildiv(C[1], 2);
		} else if (P == 3) {
			int mn = min(C[1], C[2]);
			ans += mn;
			ans += ceildiv(C[1] - mn, 3);
			ans += ceildiv(C[2] - mn, 3);
		} else if (P == 4) {
			ans += C[2] / 2;
			C[2] %= 2;

			int mn = min(C[1], C[3]);
			ans += mn;
			C[1] -= mn;
			C[3] -= mn;

			if (C[2] >= 1 && C[1] >= 2) {
				ans++;
				C[2]--;
				C[1] -= 2;
			}

			if (C[2] >= 1 && C[3] >= 2) {
				ans++;
				C[2]--;
				C[3] -= 2;
			}

			if (C[1] == 0 && C[3] == 0) {
				if (C[2] >= 1) {
					ans++;
				}
			} else {
				ans += ceildiv(C[1], 4);
				ans += ceildiv(C[3], 4);
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
