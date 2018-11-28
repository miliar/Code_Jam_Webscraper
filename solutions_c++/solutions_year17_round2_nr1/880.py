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






int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);
		int D, N; scanf("%d%d", &D, &N);

		double t = 0;
		FOR(zz, N) {
			int K, S; scanf("%d%d", &K, &S);
			//printf("%d %d\n", K, S);
			t = max(t, double(D - K) / S);
		}

		double ans = D / t;

		printf("%.10lf\n", ans);


	}


	return 0;
}
