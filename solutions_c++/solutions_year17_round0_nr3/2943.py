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
	unsigned long long N, K, P;
	scanf("%d", &tc);
	for (int t = 0; t < tc; ++t) {
		scanf("%I64u %I64u", &N, &K);
		printf("Case #%d: ", t + 1);
		/*if (2 * K - 1 >= N ) {
			printf("0 0\n");
		} else {*/
			P = K;
			long long l = 1;
			while (P) {
				P >>= 1;
				l <<= 1;
			}
			l++;
			l/=2;
			long long ans1 = (N - l) / l;
			long long ans2 = (N - l) % l;

			if ((K - l) <= ans2) ans1++;
			ans2 = (ans1 - 1) / 2;
			ans1 /= 2;

			printf("%I64u %I64u\n", ans1, ans2);

		//}
	}
	fclose (stdout);
	fclose (stdin);
	return 0;
}