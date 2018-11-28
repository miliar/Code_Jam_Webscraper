//#include <stdio.h>
#include <bits/stdc++.h>
//#include <ctime>

using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

typedef long double LD;
typedef pair<LL,LL> PLL;
typedef vector <PLL> VPLL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

const int maxn=1e4;
int T;
int d,n;
LD arrival,s,x;

int main()
{
	cin>>T;
	FOR(t,1,T)
	{
		cin>>d>>n;
		arrival=0.0;
		REP(i,n)
		{
			cin>>s>>x;
			arrival=max(arrival,(d-s)/x);
		}
		
		cout<<fixed;
		cout.precision(10);
		cout<<"Case #"<<t<<": "<<d/arrival<<endl;
	
	}

}






