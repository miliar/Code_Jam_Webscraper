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

LL n;
int t;
string s,a,b;
string dodaj(string slo, int pos, int over)
{
	//cout<<"dodaj == "<<slo<<" "<<pos<<" "<<over<<endl;
	if(pos==SIZE(s))
	return slo;

	string wyn;
	if(over==0)
	{
		wyn.clear();
		FORD(c,s[pos],slo.back())
		{
			wyn.clear();
			wyn=dodaj(slo+(char(c)),pos+1,over|=(c!=s[pos]));
			if(!wyn.empty())
			{
				return wyn;
			}
		}
	}
	else
	{
		wyn.clear();
		FORD(c,'9',slo.back())
		{
			wyn.clear();
			wyn=dodaj(slo+(char(c)),pos+1,over);
			if(!wyn.empty())
			{
				return wyn;
			}
		}
	}
	wyn.clear();
	return wyn;
}
string solve()
{
	string temp;
	temp.clear();
	FORD(i,s[0],'1')
	{
		temp.clear();
		temp=temp+(char(i));
		temp=dodaj(temp,1,(i!=s[0]));
		if(!temp.empty())
		return temp;
	}
	temp.clear();
	return temp;
}
int main()
{
	cin>>t;
	REP(tt,t)
	{
		cin>>n;
		s=to_string(n);
		a.clear();
		REP(i,SIZE(s)-1)
		a=a+'9';
		
		b=solve();
		if(SIZE(b)>SIZE(a))
		{
			a=b;
		}
		cout<<"Case #"<<tt+1<<": "<<a<<endl;
	}

}






