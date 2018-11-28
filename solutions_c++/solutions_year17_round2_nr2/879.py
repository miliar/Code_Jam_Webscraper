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

int T;
int n,r,o,y,g,b,v;
string odp;
pair <int,char> tab[3];
int main()
{
	cin>>T;
	FOR(t,1,T)
	{
	
		cout<<"Case #"<<t<<": ";
		cerr<<endl;
		cin>>n;
		cin>>r>>o>>y>>g>>b>>v;
	
		if(o!=0)
		{
			if((o+b)==n)
			{
				if(o!=b)
				{
					cerr<<"if";
					cout<<"IMPOSSIBLE"<<endl;
					continue;
				}
			}
			else
			{
				if(b-o<1)
				{
					cerr<<"if";
					cout<<"IMPOSSIBLE"<<endl;
					continue;
				}
			}
		}
		#define o g
		#define b r
		if(o!=0)
		{
			if((o+b)==n)
			{
				if(o!=b)
				{
					cerr<<"if";
					cout<<"IMPOSSIBLE"<<endl;
					continue;
				}
			}
			else
			{
				if(b-o<1)
				{
					cerr<<"if";
					cout<<"IMPOSSIBLE"<<endl;
					continue;
				}
			}
		}
		#undef o
		#undef b
		#define o v
		#define b y
		if(o!=0)
		{
			if((o+b)==n)
			{
				if(o!=b)
				{
					cerr<<"if";
					cout<<"IMPOSSIBLE"<<endl;
					continue;
				}
			}
			else
			{
				if(b-o<1)
				{
					cerr<<"if";
					cout<<"IMPOSSIBLE"<<endl;
					continue;
				}
			}
		}
		#undef o
		#undef b
		/*
		if( ((b+o)==n && (b!=o)) || ((r+g)==n && (r!=g)) || ((y+v)==n && (y!=v))  )	
		{
			cerr<<"if";
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		*/
		b-=o;
		r-=g;
		y-=v;
		
		odp.clear();
		
		
		
		tab[0]=MP(b,'B');
		tab[1]=MP(y,'Y');
		tab[2]=MP(r,'R');
			
		sort(tab,tab+3);
		if(tab[2].ST>(tab[0].ST+tab[1].ST))
		{
			cerr<<"if2";
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		int nadmiar=tab[1].ST+tab[0].ST-tab[2].ST;
		
		REP(i,nadmiar)
		{
	
			odp=odp+tab[2].ND+tab[1].ND+tab[0].ND;
			tab[0].ST--;
			tab[1].ST--;
			tab[2].ST--;
		}
		while(tab[2].ST>0)
		{

			odp=odp+tab[2].ND;
			tab[2].ST--;
			if(tab[1].ST>0)
			{
				tab[1].ST--;
				odp=odp+tab[1].ND;
			}
			else if(tab[0].ST>0)
			{
				tab[0].ST--;
				odp=odp+tab[0].ND;
			}
			else
			{
				cout<<"klopot";
				cerr<<"impossible event"<<endl;
			}
		}
		
		//output
		if(odp.empty())
		{
			REP(i,v)
			{
				cout<<"YV";
			}
			REP(i,g)
			{
				cout<<"RG";
			}
			REP(i,o)
			{
				cout<<"BO";
			}
			cout<<endl;
		}
		else
		{

			bool rf,yf,bf;
			rf=yf=bf=true;
			REP(i,SIZE(odp))
			{
				cout<<odp[i];
				if(odp[i]=='R' && rf)
				{
					rf=false;
					REP(xx,g)
					cout<<"GR";
				}
				if(odp[i]=='Y' && yf)
				{
					yf=false;
					REP(xx,v)
					cout<<"VY";
				}
				if(odp[i]=='B' && bf)
				{
					bf=false;
					REP(xx,o)
					cout<<"OB";
				}
			}
			cout<<endl;
		}
	}
}






