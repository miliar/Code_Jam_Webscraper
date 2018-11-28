#include<bits/stdc++.h>
#include<cmath>

#define pc(x) putchar_unlocked(x);
#define forn(i, n) for(int i=0;i<(int)(n);i++)
#define forin(i, k, n) for(int i=k;i<(int)(n);i++)
#define pb push_back
#define zero(x) memset(x, 0, sizeof x);

using namespace std;
using ll = long long;
using iptr = shared_ptr<int>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vii = vector<pii>;
using mii = map<int, int>;
using si = set<int>;

// inline int Read()
// {
//  register int c=getchar_unlocked();
//  int x=0;
//  for(;(c<48 || c>57);c=getchar_unlocked());
//  for(;c>47 && c<58;c=getchar_unlocked())
//      x=(x<<1)+(x<<3)+c-48;
//  return x;
// }

inline ll Read()
{
	register int c=getchar_unlocked();
	ll x=0;
	for(;(c<48 || c>57);c=getchar_unlocked());
	for(;c>47 && c<58;c=getchar_unlocked())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

inline void ReadAI(int *a, int n)
{
	for(int i=0;i<n;i++)
		a[i]=Read();
}

void ReadALL(ll *a, ll n)
{
	for(ll i=0;i<n;i++)
		a[i]=Read();
}

int main()
{
	using pdd = pair<double, double>;
	const double pi = 3.14159265358979323846;
	ll t=Read();
	struct c1
	{
		bool operator()(const pdd& left, const pdd& right) const
		{
			if(abs(left.first*left.second - right.first*right.second) < 0.000001f)
				return left.first > right.first;
			return left.first*left.second > right.first*right.second;
		}
	};
	struct c2
	{
		bool operator()(const pdd& left, const pdd& right) const
		{
			if(abs(left.first - right.first) < 0.000001f)
				return left.second > right.second;
			return left.first > right.first;
		}
	};

	forn(z, t)
	{
		ll n=Read(), k=Read();
		
		multiset<pdd, c1> srh;
		multiset<pdd, c2> srr;
		forn(i, n)
		{
			pdd a;
			a.first = double(Read());
			a.second = double(Read());
			srh.insert(a);
			srr.insert(a);
		}
		
		double ans = 0.0;
		for(auto dd: srr)
		{
			double cur = dd.first*dd.first + 2.0*dd.first*dd.second;
			auto it = srh.begin();
			int cnt = k-1;
			bool done = false;
			while(cnt && it != srh.end())
			{
				if((not done) && abs(it->first - dd.first) < 0.000001f && abs(it->second - dd.second) < 0.000001f)
				{
					it++;
					done = true;
					continue;
				}
				if(it->first <= dd.first)
				{
					cur += 2.0*it->first*it->second;
					cnt--;
				}
				it++;
			}
			ans = max(cur, ans);
		}
		
		printf("Case #%d: %.9lf\n", z+1, ans*pi);
		// cout << "Case #" << z+1 << ": " << ans << endl;
	}
	return 0;
}
