/*===============================================================
*  Filename£ºc.cpp
*  Author£ºzhuyutian
*  Date£º2017Äê04ÔÂ08ÈÕ
================================================================*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const int maxn = 100005;

int T;
ll n,k;

ll getd(ll x)
{
	ll c = 1;
	while(x) { c <<= 1; x >>= 1; }
	return c / 2;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	cin>>T;
	for(int kase = 1; kase <= T; kase ++)
	{
		cin>>n>>k;
		n -= k - 1;
		ll d = getd(k);
		ll a = 1;
		while(a < k) a *= 2;
		ll mx = n / d + (n % d > 0),mi = n / d;
		ll ans = mx;
		if(mx != mi && k - a > (n % d)) ans = mi; 
		printf("Case #%d: %lld %lld\n",kase,ans / 2,ans / 2 - (ans % 2 == 0));
		
	}
    return 0;
}
