#include <bits/stdc++.h>
using namespace std;

#define ld long double
#define pdd pair<ld,ld>
#define X first
#define Y second
const int N=1005;
pdd x[N];
pdd b[N];
int n,d;
bool valid(ld m)
{
	ld t=0;
	ld ini=0;
	ld D=d;
	while(true)
	{
		ld tmin=1e18;
		for(int i=2;i<=n+1;i++)
			if(x[i-1].Y>x[i].Y)
				if(x[i-1].X!=x[i].X)
					tmin=min(tmin,(x[i].X-x[i-1].X)/(x[i-1].Y-x[i].Y));
		//update all the x's
		//cout<<"****"<<endl;
		//cout<<tmin<<endl;
		//for(int i=1;i<=n+1;i++)
			//cout<<x[i].X<<" "<<x[i].Y<<endl;
		//cout<<"****"<<endl;
		if(tmin==1e18)
			return true;
		//cout<<"Here"<<endl;
		ini+=(tmin*m);
		t+=tmin;
		for(int i=n+1;i>=1;i--)
		{
			ld nx=x[i].X+x[i].Y*tmin;
			if(i==n+1)
			{
				x[i].X=nx;
				continue;
			}
			if(nx>=x[i+1].X)
			{
				x[i].X=x[i+1].X;
				x[i].Y=x[i+1].Y;
			}
			else
			{
				x[i].X=nx;
			}
		}
		//cout<<"****"<<endl;
		//cout<<tmin<<endl;
		//for(int i=1;i<=n+1;i++)
			//cout<<x[i].X<<" "<<x[i].Y<<endl;
		//cout<<"****"<<endl;
		if(ini>x[1].X)
			return false;
		//cout<<"HereF"<<endl;
		if(ini>=D)
			return true;
		//cout<<"Heret2"<<endl;
		if(ini==x[1].X&&m>x[1].Y)
			return false;
		//cout<<"Heref2"<<endl;
	}
	return true;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin>>t;
	int ci=1;
	while(t--)
	{
		cin>>d>>n;
		for(int i=1;i<=n;i++)
		{
			int k,s;
			cin>>k>>s;
			x[i].X=k;
			x[i].Y=s;
		}
		x[n+1]=make_pair(d,0);
		sort(x+1,x+n+1);
		//valid(360);
		//break;
		for(int i=1;i<=n+1;i++)
			b[i]=x[i];
		ld lo=0,hi=1e13;
		ld ans=0;
		for(int w=1;w<=80;w++)
		{
			for(int i=1;i<=n+1;i++)
				x[i]=b[i];
			ld m=(lo+hi)/2.0;
			if(valid(m))
			{
				ans=max(ans,m);
				lo=m;
			}
			else hi=m;
		}
		cout<<"Case #"<<ci<<": ";
		ci++;
		cout<<setprecision(25)<<ans<<endl;
	}
}
