#define LOCAL

#ifdef LOCAL
#define _GLIBCXX_DEBUG
#pragma GCC optimize("O3")
#endif
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

	int t;
	cin>>t;
	for(int ii=1; ii<=t; ii++)
	{
		DBG(ii);
		int n, c, m;
		cin>>n>>c>>m;
		vector < int > ile_biletow_osoba(1001, 0);
		vector < int > ile_biletow_miejsce(1001, 0);
		int wyn = 0;
		for(int i=0; i<m; i++)
		{
			int x, y;
			cin>>x>>y;
			y--;
			x--;
			ile_biletow_osoba[y]++;
			ile_biletow_miejsce[x]++;
			wyn = max(wyn, ile_biletow_osoba[y]);
		}
		int sp = 0;
		for(int i=0; i<1001; i++)
		{
			int akt = 0;
			sp += ile_biletow_miejsce[i];
			akt += sp/(i+1);
			if (sp % (i+1) != 0)
				akt++;
			wyn = max(akt, wyn);
		}
		int ile_promocji = 0;
		sp = 0 ;
		for(int i=0; i<1001; i++)
		{
			sp += ile_biletow_miejsce[i];
			int ipa = 0;
			ipa = max(0, sp - (i+1) * wyn);
			ipa = max(ipa, ile_biletow_miejsce[i] -  wyn);
			ile_promocji += ipa;
		}
		cout << "Case #" << ii << ": " << wyn << " " << ile_promocji << endl;
	}
	
    return 0;
}

