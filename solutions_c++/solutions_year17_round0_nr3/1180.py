#include<stdio.h>
int main()
{
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas = 1; cas <= t; cas++)
	{
		long long n, k; scanf("%lld %lld", &n, &k);
		long long x = 1;
		while(x*2 <= k) x *= 2;
		k = k-(x-1);
		n = n-(x-1);
		long long big = n%x;
	//	printf("n : %d k : %d big : %d x : %d\n", n, k, big, x);
		long long res = (k <= big)? n/x+1 : n/x;
		printf("Case #%d: %lld %lld\n", cas, (res-1)/2+(res-1)%2, (res-1)/2);
	}
}
