#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <queue>

using namespace std;

bool bad (long long n)
{
	int k = 9;
	while (n > 0)
	{
		int kk = n%10;
		if (kk > k)
			return true;
		k = kk;
		n /= 10;
	}
	return false;
}

long long solve(long long n)
{
	for (;;)
	{
		if (!bad(n))
			break;
		long long c = 10;
		while ((n%c) == c-1)
			c *= 10;
		n -= (n%c) + 1;
		//printf("%lld ", n);
	}
	return n;
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int i=0; i<T; ++i)
	{
		long long n;
		scanf("%lld\n", &n);
		printf("Case #%d: %lld\n", i+1, solve(n));
	}
	return 0;
}
