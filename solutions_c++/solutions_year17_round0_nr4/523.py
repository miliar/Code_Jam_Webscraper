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
		int n, m;
		cin>>n>>m;
		vector < vector < char > > start(n, vector < char >(n, '.'));
		vector < vector < char > > koniec(n, vector < char >(n, '.'));
		
		int ktory = -1;
		while(m--)
		{
			char c;
			int a, b;
			cin>>c>>a>>b;
			a--, b--;
			assert(a == 0);
			start[a][b] = c;//R, C // y, x
			if (c != '+' && c != '.')
			{
				assert(ktory == -1);
				ktory = b;
			}
		}
		ktory = max(ktory, 0);
		vector < tuple<char, int, int > > zmiany;
		if (n==1)
		{
			koniec[0][0] = 'o';
		}
		else
		{
			koniec[0][ktory] = 'x';
			//DBG(ktory, koniec[0][0], koniec[0][n-1]);
			for(int i=1; i<n; i++)
			{
				if (i <= ktory)
					koniec[i][i-1] = 'x';
				else
					koniec[i][i] = 'x';
			}
			for(int i=0; i<n; i++)
			{
				if (koniec[0][i] == 'x')
					koniec[0][i] = 'o';
				else
					koniec[0][i] = '+';
			}
			for(int i=1; i<n-1; i++)
			{
				if (koniec[n-1][i] == 'x')
					koniec[n-1][i] = 'o';
				else
					koniec[n-1][i] = '+';
			}
		}
		for(int i=0; i<n; i++)
			for(int j=i+1; j<n; j++)
				for(int k=0; k<n; k++)
				{
					if (koniec[k][i] != '.' && koniec[k][j] != '.' && koniec[k][i] != '+' && koniec[k][j] != '+')
						assert(false);
					if (koniec[i][k] != '.' && koniec[j][k] != '.' && koniec[i][k] != '+' && koniec[j][k] != '+')
					{
				//		DBG(test, k, i, j, koniec[i][k], koniec[j][k]);
						assert(false);
					}
					
				}
		
		
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(start[i][j] != koniec[i][j])
					zmiany.pb(tuple<char, int, int>{koniec[i][j], i+1, j+1});
		int wynik = 3*n-2;
		if (n == 1)
			wynik++;
		cout << "Case #" << test <<": " << wynik << " " << SZ(zmiany) << endl;
		for(auto& el : zmiany)
		{
			char c;
			int a, b;
			tie(c, a, b) = el;
			cout << c << " " << a << " " << b << endl;
		}
				
	}
    return 0;
}
