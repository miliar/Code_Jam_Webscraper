#include<cstdio>

typedef long long LL;

int main()
{
	int T; scanf("%d", &T);
	for (int _ = 0; _ < T; ++_)
	{
		LL N; scanf("%lld", &N);
		LL N2 = N;
		LL best = 1000000000000000000;
		int last = 0;
		bool bad = 0;
		for (LL x = best; x > 0; x/=10)
		{
			LL d = N/x;
			if (d < last) {bad = 1; break;}
			if (d > last) {best = x; last = d;}
			N %= x;
		}
		if (bad)
		{
			N2 -= best; best /= 10;
			while (best > 0)
			{
				N2 += (9 - (N2/best)%10) * best;
				best /= 10;
			}
		}
		printf("Case #%d: %lld\n", _+1, N2);
	}
	return 0;
}
