#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;




double p[53];

int main() {
	freopen("C-small-1-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);

		int N, K; scanf("%d%d", &N, &K);
		double U; scanf("%lf", &U);
		FOR(i, N) scanf("%lf", &p[i]);


		

		sort(p, p+N);
		p[N] = 1;

		FOR(i, N) {
			double ideal = (i+1)*(p[i+1] - p[i]);

			double d = min(U, ideal);
			for (int j=0; j<=i; j++)
				p[j] += d / (i+1);

			U -= d;
		}


		double ans = 1;
		FOR(i, N) ans *= p[i];
		printf("%.10lf\n", ans);


		




	}

	return 0;
}
