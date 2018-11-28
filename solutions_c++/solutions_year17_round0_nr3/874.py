#include <bits/stdc++.h>
using namespace std;
const int N = 2010;
typedef long long ll;
int mod = 1000000007;

void run()
{
	ll n, k;
	scanf("%lld%lld", &n, &k);
	while (k > 1)
	{
		if (k&1)
		{
			n = (n-1)>>1;
		}else
			n >>= 1;
		k>>=1;
	}
	printf("%lld %lld\n", (n>>1), (n-1)>>1);
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	scanf("%d", &T);
	 
	while (T--)
	{ 
		printf("Case #%d: ", cas++);
		run();
	}
    return 0;
}