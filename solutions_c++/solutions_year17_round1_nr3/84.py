#include<bits/stdc++.h>
#define rep(i,k,n) for(ll i= (ll) k;i< (ll) n;i++)
#define all(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;

using namespace std;

template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}

#define LOCAL
#ifdef LOCAL
#define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define DBG(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif

ll Hd, Ad, Hk, Ak, B, D;

ll rob(ll debuff, ll buff)
{
	ll Ahd = Hd;
	ll AAd = Ad;
	ll AHk = Hk;
	ll AAk = Ak;
	ll wyn = 0;
	for(int i=0; i<500; i++)
	{
//		DBG(debuff);
//		DBG(AHk, Ahd, AAk, AAd, debuff, buff);
		wyn++;
		if (AHk <= AAd)
			return wyn;
			
		if ( (debuff && AAk - D >= Ahd) || (debuff == 0 && AAk>= Ahd) )
		{
			Ahd = Hd;
		}
		else if (debuff)
		{
			debuff--;
			AAk = max(0ll, AAk - D);
		}
		else if (buff)
		{
			buff--;
			AAd = AAd + B;
		}
		else
		{
			AHk -= AAd;
		}
		Ahd -= AAk;
	}
	return wyn;
}

bool possible()
{
	if (Ad >= Hk)
		return true;
	if (Ak - D >= Hd)
		return false;
	return true;
}

int main()
{
#ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#endif

	int t;
	cin>>t;
	for(int test=1; test<=t; test++)
	{
		DBG(test);
		cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
		ll min_wyn = IINF;
		for(int i=0; i<=100; i++)
			for(int j=0; j<=100; j++)
			{
				//DBG(i, j);
				min_wyn = min(min_wyn, rob(i, j));
			}
				
		if (possible() && min_wyn < 500)
			cout<<"Case #"<<test<<": " << min_wyn << "\n";
		else
			cout<<"Case #"<<test<<": " << "IMPOSSIBLE" << "\n";
				
	}
    return 0;
}
