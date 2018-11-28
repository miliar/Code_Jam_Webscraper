#include<bits/stdc++.h>
#include<cmath>

#define forn(i, n) for(int i=0;i<(int)(n);i++)
#define forin(i, k, n) for(int i=k;i<(int)(n);i++)

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vii = vector<pii>;
using mii = map<int, int>;
using si = set<int>;

// inline int Read()
// {
// 	register int c=getchar();
// 	int x=0;
// 	for(;(c<48 || c>57);c=getchar());
// 	for(;c>47 && c<58;c=getchar())
// 		x=(x<<1)+(x<<3)+c-48;
// 	return x;
// }

// inline void ReadAI(int *a, int n)
// {
// 	for(int i=0;i<n;i++)
// 		a[i]=Read();
// }

inline ll Read()
{
	register int c=getchar();
	ll x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

void ReadALL(ll *a, ll n)
{
	for(ll i=0;i<n;i++)
		a[i]=Read();
}

int main()
{
	int t=Read();
	forin(test, 1, t+1)
	{
		ll n = Read(), k = Read(), last;
		multiset<ll, greater<ll>> s;
		s.insert(n);
		while(k && not s.empty())
		{
			k--;
			auto first = *s.begin();
			last = first;
			s.erase(s.begin());
			auto half = first >> 1;
			if(half == 0)
			{
				s.insert(0);
				s.insert(0);
				continue;
			}
			s.insert(half);
			if(first&1)
				s.insert(half);
			else
				s.insert(half - 1LL);
		}
		auto a1 = last >> 1;
		auto a2 = (last & 1) ? a1 : (a1 - 1LL);
		printf("Case #%d: %lld %lld\n", test, a1, a2);
	}
}
