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

const int maxn=1e3+100;
int n,t,k;
string s;
char tab[maxn];
inline void flip(const int &x)
{
	REP(p,k)
	{
		s[x+p]=(s[x+p]=='-' ? '+' : '-');
	}
}
int solve()
{
	int wyn=0;
	cin>>s>>k;
	REP(i,SIZE(s)-k+1)
	{
		if(s[i]=='-')
		{
			wyn++;
			flip(i);
		}
	}
	REP(i,SIZE(s))
	{
		if(s[i]=='-')
		return -1;
	}
	return wyn;
}
int main()
{
	cin>>t;
	int ret;
	REP(tt,t)
	{	
		printf("Case #%d: ",tt+1);
		if((ret=solve())==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ret);
	}
}






