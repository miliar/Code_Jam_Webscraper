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


char m[26][26];
struct Prostokat
{
	ll x1, x2;
	ll y1, y2;
	char c;
	bitset < 300 > srodek(ll xx1, ll xx2, ll yy1, ll yy2)
	{
		bitset < 300 > B(0);
		for(int x = xx1; x<=xx2; x++)
			for(int y = yy1; y<=yy2; y++)
			{
				if (m[x][y] != '?')
				{
					B[ m[x][y] ] = 1;
					c = m[x][y];
				}
			}
		return B;
	}
	bool ok()
	{
		auto B = srodek(x1, x2, y1, y2);
		//DBG(B);
		return B.count() == 1;
	}
	void maluj()
	{
		for(int x = x1; x<=x2; x++)
			for(int y = y1; y<=y2; y++)
			{
				m[x][y] = c;
			}
	}
	void dziel(Prostokat& p1, Prostokat& p2)
	{
		for(int i=x1; i<x2; i++)
		{
			p1 = (*this);
			p2 = (*this);
			p1.x2 = i;
			p2.x1 = i+1;
			auto B1 = p1.srodek(p1.x1, p1.x2, p1.y1, p1.y2);
			auto B2 = p2.srodek(p2.x1, p2.x2, p2.y1, p2.y2);
			if (B1.count() && B2.count() && (B1 & B2).count() == 0 )
				return;
		}
		for(int i=y1; i<y2; i++)
		{
			p1 = (*this);
			p2 = (*this);
			p1.y2 = i;
			p2.y1 = i+1;
			auto B1 = p1.srodek(p1.x1, p1.x2, p1.y1, p1.y2);
			auto B2 = p2.srodek(p2.x1, p2.x2, p2.y1, p2.y2);
			//DBG(B1.count(), B2.count(), (B1 & B2).count() == 0);
			if (B1.count() && B2.count() && (B1 & B2).count() == 0 )
				return;
		}
		
	}
};



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
		ll R, C;
		cin>>R>>C;
		for(int i=1; i<=R; i++)
			for(int j=1; j<=C; j++)
				cin>>m[i][j];
		vector < Prostokat > P(1, Prostokat{1, R, 1, C, '1'});
		while(SZ(P))
		{
			auto pro = P.back();
		//	DBG(test, pro.x1, pro.x1, pro.y1, pro.y2);
			P.pop_back();
			if (pro.ok())
			{
				pro.maluj();
			}
			else
			{
				Prostokat p1, p2;
				pro.dziel(p1, p2);
				P.pb(p1);
				P.pb(p2);
			}			
		}
		cout<<"Case #"<<test<<":\n";
		
		for(int i=1; i<=R; i++)
		{
			for(int j=1; j<=C; j++)
				cout<<m[i][j];
			cout<<endl;
		}
		
	}
    return 0;
}
