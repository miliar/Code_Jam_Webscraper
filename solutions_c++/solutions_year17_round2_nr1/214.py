#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int T;
int D, N;

int main() {
	int T0 = 0;
	scanf("%d", &T);
	for ( ; T; --T) {
		cin >> D >> N;
		double ans = 1e100;
		for (int i = 0; i < N; ++i) {
			double k, s;
			cin >> k >> s;
			double ti = (D - k) / s;
			ans = min(ans, D / ti);
		}
		printf("Case #%d: %.6lf\n", ++T0, ans);
	}
	return 0;
}