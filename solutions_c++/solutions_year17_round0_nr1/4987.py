#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <utility>

#define fi first
#define se second
#define mp make_pair
#define PI 3.14159265
#define INF 1023123123
#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c; --a)

using namespace std;

int main() {
	int T, K;
	char pancake[1005];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		scanf("%s %d", pancake, &K);

		int ans = 0;
		int n = strlen(pancake);

		for (int i = 0; i <= n - K; ++i) {
			if (pancake[i] == '-') {
				++ans;

				REP(j, K) {
					pancake[i + j] = pancake[i + j] == '-' ? '+' : '-';
				}
			}
		}

		int possible = true;

		REP(i, n)
			possible = possible && (pancake[i] == '+');

		if (possible)
			printf("Case #%d: %d\n", tc, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}

	return 0;
}