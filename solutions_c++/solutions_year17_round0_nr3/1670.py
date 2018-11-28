#include <bits/stdc++.h>
using namespace std;
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
#define foreach(x, y) for(__typeof(y.begin()) x = y.begin(); x != y.end(); ++x)
#define rforeach(x, y) for(__typeof(y.rbegin()) x = y.rbegin(); x != y.rend(); ++x)
typedef long long ll;

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		ll n, k; cin >> n >> k;
		map<ll, ll> s;
		s[n] = 1;
		for(;;)
		{
			ll ss = 0;
			for(auto p: s)
				ss += p.second;
			if(k <= ss)
				break;
			k -= ss;
			map<ll, ll> t;
			for(auto p: s)
			{
				{
					ll c = p.first / 2;
					if(c)
						t[c] += p.second;
				}
				{
					ll c = (p.first - 1) / 2;
					if(c)
						t[c] += p.second;
				}
			}
			s = t;
		}
		rforeach(it, s)
			if(k > it->second)
				k -= it->second;
			else
			{
				printf("Case #%d: ", _);
				cout << it->first / 2 << ' ' << (it->first - 1) / 2 << endl;
				break;
			}
	}
	return 0;
}