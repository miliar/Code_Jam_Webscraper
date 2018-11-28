#include <cstdio>
#define ll long long
ll N;
int L;
int length(ll n)
{
	int l = 0;
	while(n != 0)
	{
		++l;
		n /= 10;
	}
	return l;
}
ll getMax(int n, int last, ll p, ll sum)
{
	if(sum > N) return -1;
	if(n == L + 1) return sum;
	for(int i = 9; i >= last; i--)
	{
		ll x = getMax(n + 1, i, p / 10, sum + p * i);
		if(x != -1) return x;
	}
	return -1;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%lld", &N);
		L = length(N);
		ll p = 1;
		for(int i = 0; i < L - 1; i++) p *= 10;
		ll Max = getMax(1, 1, p, 0);
		printf("Case #%d: %lld\n", t, Max == -1 ? p - 1 : Max);
	}
}
