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
		map < ll, ll > M[100];
		ll n, k;
		cin>>n>>k;
		M[0][n] = 1;
		vector < pair < ll, ll > > V;
		for(int i=0; SZ(M[i]); i++)
		{
			for(auto el : M[i])
			{
				V.pb(el);
				ll l = (el.ft-1)/2;
				ll p = (el.ft-1) - l;
				if (p > 0)
					M[i+1][p] += el.sd;
				if (l > 0)
					M[i+1][l] += el.sd;
			}
		}
		sort(V.rbegin(), V.rend());
		//for(auto& el : V)
		//	printf("(%lld, %lld) ", el.ft, el.sd);
		//cout << endl;
		
		ll wyn = 0;
		ll akt = 0;
		for(int i=0; i<SZ(V); i++)
		{
			akt += V[i].sd;
			if (akt >= k)
			{
				wyn = V[i].ft;
				break;
			}
		}
		ll l = (wyn-1)/2;
		ll p = (wyn-1) - l;
		cout<<"Case #"<<test<<": "<<" ";
		cout<<p << " " << l;
		cout << endl;		
	}
    return 0;
}
