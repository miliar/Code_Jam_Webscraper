#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"

using namespace std;

#define ll long long

char s[100];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		ll n, k;
		scanf("%lld%lld", &n, &k);
		ll x = 1;
		while (1)
        {
            if (((1LL<<x)-1) >= k)
            {
                break;
            }
            x++;
        }
		x--;
		ll tmp = k - ((1LL<<x)-1);
		ll cnt = n - ((1LL<<x)-1);
		ll ans = cnt / (1LL<<x);
		if (tmp <= cnt % (1LL<<x))
		{
			ans++;
		}
		printf("Case #%d: %lld %lld\n", cas, ans/2, ans%2LL==0 ? ans/2-1 : ans/2);
	}
	return true;
}
