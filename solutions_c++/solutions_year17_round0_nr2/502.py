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


ll pot(int x)
{
	ll wyn = 1;
	while(x--)
		wyn *= 10;
	return wyn;
}

bool ok(ll liczba)
{
	if (liczba < 10)
		return true;
	vector < int > V;
	while(liczba > 0)
	{
		V.pb(liczba%10);
		liczba/= 10;
	}
	for(int i=0; i+1 < SZ(V); i++)
		if (V[i] < V[i+1])
			return false;
	return true;
}

int main()
{
#ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#endif
	int testy;
	cin>>testy;
	for(int test = 1; test <= testy; test++)
	{
		ll s;
		cin>>s;
		ll wyn;
		if (ok(s))
		{
			wyn = s;
		}
		else
		{
			
			wyn = 9;
			while(wyn <= s)
				wyn = 10ll*wyn + 9;
			wyn /= 10;
			for(int i=0; pot(i) < s; i++)
			{
				ll temp = s;
				ll p = pot(i);
				temp -= temp%p;
				temp--;
				if (ok(temp))
				{
					wyn = temp;
					break;
				}
			}
			/*
			wyn = 0;
			for(int i=0; i<=s; i++)
				if ( ok(i) )
					wyn = i;*/
		}
		cout<<"Case #"<<test<<": "<<" ";
		cout<<wyn;
		cout << endl;		
	}
    return 0;
}
