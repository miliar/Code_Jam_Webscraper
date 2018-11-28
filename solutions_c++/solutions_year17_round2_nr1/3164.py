#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	freopen("inp.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc;

	scanf("%d", &tc);
	for (int t = 0; t < tc; ++t) {
		int D, A;
		scanf("%d %d", &D, &A);
		int k, s;
		long double time = 0, buf_t = 0;
		scanf("%d %d", &k, &s);
		time = D - k;
		time /= s;
		buf_t = time;
		for (int i = 1; i < A; ++i) {
			scanf("%d %d", &k, &s);
			int p = D - k; 
			time = (long double)p / (long double)s;
			if (time > buf_t)
				buf_t = time;
		}
		long double ans = D;
		ans /= buf_t;
		printf("Case #%d: ", t + 1);
		printf ("%.6llf\n", ans);
	}
	fclose (stdout);
	fclose (stdin);
	return 0;
}