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
#define PI acos(-1);
#define INF 1023123123
#define pll pair <long long int, long long int>
#define pii pair <int, int>
#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c; --a)

using namespace std;

int main() {
	int Ac, Aj, T;
	pii cameron[105], jamie[105];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		int ans = 2000;

		scanf("%d %d", &Ac, &Aj);

		REP(i, Ac)
			scanf("%d %d", &cameron[i].fi, &cameron[i].se);

		REP(i, Aj)
			scanf("%d %d", &jamie[i].fi, &jamie[i].se);

		sort(cameron, cameron + Ac);
		sort(jamie, jamie + Aj);

		if (Ac == 2) {
			int resJam = 720 - ((cameron[0].se - cameron[0].fi) + (cameron[1].se - cameron[1].fi));

			if (resJam >= cameron[1].fi - cameron[0].se) {
				ans = 2;
			}
			else {
				ans = 4;

				int a = cameron[0].fi;
				int b = 1440 - cameron[1].se;

				if (a + b <= resJam)
					ans = 2;
			}
		}
		else if (Aj == 2) {
			int resCam = 720 - ((jamie[0].se - jamie[0].fi) + (jamie[1].se - jamie[1].fi));

			if (resCam >= jamie[1].fi - jamie[0].se) {
				ans = 2;
			}
			else {
				ans = 4;

				int a = jamie[0].fi;
				int b = 1440 - jamie[1].se;

				if (a + b <= resCam)
					ans = 2;
			}
		}
		else if (Ac == 1 || Aj == 1) {
			ans = 2;
		}

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}