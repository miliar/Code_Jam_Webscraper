#include<cstdio>
#include<cmath>
#pragma warning(disable:4996)
int main()
{
	freopen("file.txt","w",stdout);
	long long int N,k,n;
	scanf("%lld", &n);
	for (long long int i = 1; i <= n; ++i)
	{
		scanf("%lld %lld", &N, &k);
		int t = log2(k);
		long long int temp = powl(2, t);
		long int x = k - temp+1;
		long long int y = (N-temp+1) / temp;
		if (x <= (N-temp+1) % temp)
			++y;
		if(y%2)
			printf("Case #%lld: %lld %lld\n", i, y/2, y/2);
		else
			printf("Case #%lld: %lld %lld\n", i, y / 2, y / 2-1);

	}
}