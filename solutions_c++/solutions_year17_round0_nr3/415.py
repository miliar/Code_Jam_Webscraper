/* 2017.4.8 Celicath */
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stdint.h>

FILE* fin = fopen("input.txt", "r");
FILE* fout = fopen("output.txt", "w");

int main()
{
	int T;
	fscanf(fin, "%d", &T);

	for (int c_n = 1; c_n <= T; c_n++)
	{
		long long N, K;
		fscanf(fin, "%lld%lld", &N, &K);

		std::map<long long, long long> map;
		map[-N] = 1;
		long long L, R;
		while (K > 0)
		{
			long long n = -map.begin()->first;
			long long k = map.begin()->second;
			L = (n - 1) / 2;
			R = n - 1 - L;

			map[-L] += k;
			map[-R] += k;
			map.erase(-n);

			K -= k;
		}
		fprintf(fout, "Case #%d: %lld %lld\n", c_n, R, L);
		printf("Case #%d: %lld %lld\n", c_n, R, L);
	}
	return -0;
}
