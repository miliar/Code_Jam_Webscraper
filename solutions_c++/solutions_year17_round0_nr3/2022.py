#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

long long GetNearestPowerOfTwo(long long n)
{
	long long powerOfTwo = 2;
	while (powerOfTwo <= n)
	{
		powerOfTwo *= 2;
	}

	return powerOfTwo / 2;
}

long long GetMax(long long N, long long K);
long long GetMin(long long N, long long K);

long long GetParentValue(long long N, long long K)
{
	long long nearestPowerOfTwo = GetNearestPowerOfTwo(K);
	// 작은 것들 중에 골라야 함
	if (K - nearestPowerOfTwo >= nearestPowerOfTwo / 2)
	{
		return GetMin(N, K - nearestPowerOfTwo);
	}
	else
	{
		return GetMax(N, K - nearestPowerOfTwo / 2);
	}
}

long long GetMax(long long N, long long K)
{
	if (K == 1)
	{
		return N / 2;
	}
	
	return GetParentValue(N, K) / 2;
}

long long GetMin(long long N, long long K)
{
	if (K == 1)
	{
		return (N - 1) / 2;
	}

	return (GetParentValue(N, K) - 1) / 2;
}

pair<long long, long long> Solve(long long N, long long K)
{
	long long maxVal = GetMax(N, K);
	long long minVal = GetMin(N, K);

	return make_pair(maxVal, minVal);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		long long N, K;
		scanf("%lld %lld", &N, &K);

		pair<long long, long long> ans = Solve(N, K);
		printf("Case #%d: %lld %lld\n", i, ans.first, ans.second);
	}

	return 0;
}