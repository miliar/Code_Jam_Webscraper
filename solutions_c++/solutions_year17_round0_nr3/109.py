#include <stdio.h>
#include <iostream>
#include <string>

void solve()
{
	long long int N, K;

	scanf("%lld %lld", &N, &K);

	long long int two = 1;

	while (two * 2 <= K)
	{
		two = two * 2;
	}

	long long int mod = K % two;

	long long int val = (N - mod) / two;

	printf("%lld %lld\n", val / 2, (val - 1) / 2);
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}