#include <cstdio>
#include <iostream>

using namespace std;

int main () {
	ios_base::sync_with_stdio (false), cin.tie (nullptr);

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int tc = 0; tc < t; tc++) {
		int n;
		long long d;
		scanf ("%lld %d", &d, &n);

		long double tMax = 0;
		for(int i = 0; i < n; i++) {
			long long k, s;
			scanf ("%lld %lld", &k, &s);
			long double tCur = (d - k) / static_cast<long double> (s);
			if (tCur > tMax)
				tMax = tCur;
		}
		
		long double result = d / tMax;

		printf ("Case #%d: %.6f\n", tc + 1, result);
	}


	fflush (stdout);
	fclose (stdin);
	fclose (stdout);

	return 0;
}
