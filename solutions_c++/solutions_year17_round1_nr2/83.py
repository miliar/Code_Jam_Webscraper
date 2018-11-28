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

ll n, k;
ll sklad[1001];
vector < vector < pair < ll, ll > > > V(n);
ll wyn = 0;

bool dol(ll mam, ll potrzeba)
{
	return (mam * 10ll >= potrzeba*9ll);
}
bool gora(ll mam, ll potrzeba)
{
	return (mam*10ll <= potrzeba*11ll);
}

pair < ll, ll > wez(int z)
{
	ll x;
	cin>>x;
	ll minimum = 0, maksimum=0;
	
	ll pp = 0, kk = 11111111;
	while(kk - pp > 1)
	{
		ll s = (pp + kk)/2ll;
		if (gora(x, sklad[z]*s))
			kk = s;
		else
			pp = s;
	//	DBG(kk, pp);
	}
//	DBG(kk); 
	if (kk == 0 || !dol(x, sklad[z]*kk))
		return {0, 0};
	maksimum = minimum = kk;
		
	
	pp = 0, kk = 11111111;
	while(kk - pp > 1)
	{
		ll s = (pp + kk)/2ll;
		if (dol(x, sklad[z]*s))
			pp = s;
		else
			kk = s;
	//	DBG(kk, pp);
	}
	maksimum = pp;
	return {minimum, maksimum};
	/*
	for(ll i=1; i<=1100000; i++)
	{
		if (dol(x, sklad[z]*i) && gora(x, sklad[z]*i) )
		{
			maksimum = i;
			if (!minimum)
				minimum = i;
			
		}
	}
	return { minimum, maksimum };
	*/
	
	
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
		cin>>n>>k;
		for(int i=0; i<n; i++)
			cin>>sklad[i];
		V.clear();
		V.resize(n);
		wyn = 0;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<k; j++)
			{
				V[i].pb( wez(i));
				if (V[i].back().ft == 0)
					V[i].pop_back();
			}
			sort( V[i].rbegin(), V[i].rend());
		}
		
		int wynik = 0;
		while(true)
		{
			bool kon = false;
			for(int i=0; i<n; i++)
				if(SZ(V[i]) == 0)
					kon = true;
			if (kon)
				break;
			ll mm = -1;
			for(int i=0; i<n; i++)
				mm = max(V[i].back().ft, mm);
			bool ok = true;
			for(int i=0; i<n; i++)
				if (V[i].back().sd < mm)
				{
					ok = false;
					V[i].pop_back();
				}
			if (ok)
			{
				wynik++;
				for(int i=0; i<n; i++)
					V[i].pop_back();
			}
			
		}
		
		
		
		cout<<"Case #"<<test<<": " << wynik << "\n";		
	}
    return 0;
}
