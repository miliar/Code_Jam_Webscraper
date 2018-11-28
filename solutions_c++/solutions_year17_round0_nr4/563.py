#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

const int maxn = 110;

int al[maxn],ac[maxn],xf[maxn*2],xs[maxn*2];
int n,m,ans,M;
map<pair<int,int>,int> g;

void init()
{
	g.clear();
	ans=0;
	++M;
	cin>>n>>m;
	int l,c;
	char ch;
	while(m--)
	{
		cin>>ch>>l>>c;
		if(ch=='o' || ch=='x')
			al[l]=ac[c]=M,++ans,++g[mp(l,c)];
		if(ch=='o' || ch=='+')
			xf[l+c-1]=xs[l+n-c]=M,++ans,g[mp(l,c)]+=2;
	}
}

map<pair<int,int>,int> f;
void solve()
{
	f.clear();
	REP(i,1,n) if(al[i]!=M)
		REP(j,1,n)
			if(ac[j]!=M)
			{
				f[mp(i,j)]=1;
				++ans;
				ac[j]=M;
				break;
			}
	REP(i,1,n) if(i==1 || i==n)
		REP(j,1,n)
			if(xf[i+j-1]!=M && xs[i+n-j]!=M)
			{
				f[mp(i,j)]+=2;
				++ans;
				xf[i+j-1]=xs[i+n-j]=M;
			}
	cout<<ans<<' '<<f.size()<<endl;
	for(map<pair<int,int>,int>::iterator i=f.begin();i!=f.end();i++)
	{
		int s=i->y + g[i->x];
		if(s==1) cout<<'x';
		if(s==2) cout<<'+';
		if(s==3) cout<<'o';
		cout<<' '<<i->x.x<<' '<<i->x.y<<endl;
	}
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	cin>>T;
	REP(i,1,T)
	{
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
