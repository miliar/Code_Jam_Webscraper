#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		long long N, K;
		scanf("%lld%lld", &N, &K);
		
		long long toSub = 1;
		long long sum = N;
		while(toSub < K)
		{
			N /= 2;
			K -= toSub;
			sum -= toSub;
			toSub *= 2;
		}
		if((K - 1) * N + (toSub - K + 1) * (N - 1) >= sum)
			N--;
		
		
		// if(K > 1)
		// 	N = second;
		
		printf("Case #%d: %lld %lld\n", t, N / 2, (N - 1) / 2);
	}
}
