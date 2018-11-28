#include<stdio.h>
#define ll long long

ll solve(ll a, ll b)
{
	if(b == 0)
		return a-1;
	if(b&1)
		return solve(a/2, (b-1)/2);
	return solve((a-1)/2, (b-1)/2);
}

main()
{
	ll N, K, x;
	int k, T;
	scanf("%d", &T);
	for(k = 1; k <= T; k++)
	{
		scanf("%lld %lld", &N, &K);
		x = solve(N, K-1);
		printf("Case #%d: %lld %lld\n", k, (x+1)/2, x/2);
	}
	return 0;
}


