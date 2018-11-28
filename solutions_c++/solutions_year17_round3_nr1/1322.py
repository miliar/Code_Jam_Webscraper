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

#define M_PI 3.14159265358979323846 

int n,k;
const int maxn=1e6+6;
int T;
LD wyn;
pair <LD,LD> pan[maxn];
bool sort2(pair <LD,LD> fa, pair<LD,LD> fb)
{
	if(fa.ST*fa.ND>fb.ST*fb.ND)
	return true;
	return false;
}
LD check(int x)
{
	LD ret=pan[x].ST*pan[x].ST*M_PI+pan[x].ST*M_PI*2.0*pan[x].ND;
	vector <pair <LD,LD> > rad;
	rad.clear();
	FOR(p,x+1,n-1)
	{
		rad.PB(pan[p]);
	}
	if(SIZE(rad)<(k-1))
	{
		return (LD(0.0));
	}
	sort(ALL(rad),sort2);
	
	REP(p,k-1)
	{
		ret+=rad[p].ST*rad[p].ND*M_PI*2.0;
	}
	return ret;
}
int main()
{
	cin>>T;
	FOR(tt,1,T)
	{
		cin>>n>>k;
		REP(i,n)
		{
			cin>>pan[i].ST>>pan[i].ND;
		}
		sort(pan,pan+n);
		reverse(pan,pan+n);
		wyn=0.0;
		REP(i,n)
		wyn=max(wyn,check(i));
		cout<<fixed;
		//cerr<<M_PI<<endl;
		cout.precision(10);
		cout<<"Case #"<<tt<<": "<<wyn<<endl;
	}

}






