#include <bits/stdc++.h>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
using namespace std;
typedef long long ll;
const ll inf = (1ll << 60);

ll hd, ad, hk, ak, b, d;

ll calc(ll nDebuff, ll nBuff)
{
	ll ans = 0;
	ll hd = ::hd, ad = ::ad, hk = ::hk, ak = ::ak;
	while(nDebuff--)
	{
		if(hd <= max(ak - d, 0ll))
		{
			++ans;
			hd = ::hd - ak;
			if(hd <= max(ak - d, 0ll)) return inf;
		}
		ak = max(ak - d, 0ll);
		hd -= ak;
		++ans;
	}
	while(nBuff--)
	{
		if(hd <= ak)
		{
			++ans;
			hd = ::hd - ak;
			if(hd <= ak) return inf;
		}
		ad += b;
		hd -= ak;
		++ans;
	}
	while(hk > 0)
	{
		if(hk > ad && hd <= ak)
		{
			++ans;
			hd = ::hd - ak;
			if(hd <= ak) return inf;
		}
		hk -= ad;
		hd -= ak;
		++ans;
	}
	return ans;
}

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		cin >> hd >> ad >> hk >> ak >> b >> d;
		ll ans = inf;
		f(i, 0, 100) f(j, 0, 100)
		{
			// printf("ans %d %d %I64d\n", i, j, calc(i, j));
			ans = min(calc(i, j), ans);
		}
		if(ans >= inf) printf("Case #%d: IMPOSSIBLE\n", _); else printf("Case #%d: ", _), cout << ans << endl;
	}
	return 0;
}
