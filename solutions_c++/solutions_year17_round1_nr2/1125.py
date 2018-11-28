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

bool isValid(int stock, int require) {
	if ((require * 9 <= stock * 10) && (stock * 10 <= require * 11))
		return true;

	return false;
}

int main() {
	int T;

	scanf("%d", &T);

	FORU(tc, 1, T) {
		int N, P;
		int permu[11];
		int req[11], item[11][11];

		scanf("%d %d", &N, &P);

		REP(i, N)
			scanf("%d", &req[i]);

		REP(i, N) {
			REP(j, P)
				scanf("%d", &item[i][j]);
		}

		int ans = 0;

		if (N == 1) {
			REP(i, P) {
				int atas = (int)(floor((item[0][i] * 10) / (double)(req[0] * 9)) + 5e-9);
				int bawah = (int)(ceil((item[0][i] * 10) / (double)(req[0] * 11)) + 5e-9);

				while (!isValid(item[0][i], req[0] * bawah) && bawah <= atas)
					++bawah;

				if (bawah <= atas)
					++ans;
			}
		}
		else {
			REP(i, P)
				permu[i] = i;

			do {
				int currAns = 0;

				REP(i, P) {
					bool valid = true;

					int atas1 = (int)(floor((item[0][i] * 10) / (double)(req[0] * 9)) + 5e-9);
					int bawah1 = (int)(ceil((item[0][i] * 10) / (double)(req[0] * 11)) + 5e-9);
					int atas2 = (int)(floor((item[1][permu[i]] * 10) / (double)(req[1] * 9)) + 5e-9);
					int bawah2 = (int)(ceil((item[1][permu[i]] * 10) / (double)(req[1] * 11)) + 5e-9);

					while (!isValid(item[0][i], req[0] * bawah1) && bawah1 <= atas1)
						++bawah1;

					if (!isValid(item[0][i], req[0] * atas1))
						--atas1;

					while (!isValid(item[1][permu[i]], req[1] * bawah2) && bawah2 <= atas2) {
						++bawah2;
					}
					
					if (!isValid(item[1][permu[i]], req[1] * atas2))
						--atas2;
					
					if (bawah1 > atas1)
						valid = false;

					if (bawah2 > atas2)
						valid = false;

					if (atas2 < bawah1 || bawah2 > atas1)
						valid = false;

					if (valid) {
						++currAns;
					}
				}

				ans = max(ans, currAns);
			} while (next_permutation(permu, permu + P));

		}

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}