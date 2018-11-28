#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll T;
const ll INF=1e15;
ll d[105];
double v[105];
ll dis[105][105];
double t[105][105];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	cin>>T;
	//cout<<T<<endl;
	for(ll ca=1;ca<=T;ca++)
	{
		printf("Case #%lld: ",ca);
		ll n,q;
		cin>>n>>q;
		//cout<<q<<endl;
		for(ll i=1;i<=n;i++)scanf("%lld%lf",d+i,v+i);

				for(ll i=1;i<=n;i++)
				for(ll j=1;j<=n;j++)
				{//cout<<q<<endl;
					ll z;
					scanf("%lld",&z);
				//	cout<<z<<endl;
					//if(z==-1)z=INF;
					dis[i][j]=z;
				}

				for(ll i=1;i<=n;i++)
				{
					for(ll j=1;j<=n;j++)
						for(ll k=1;k<=n;k++)
						{
							if(dis[j][i]!=-1&&dis[i][k]!=-1)
								{
									if(dis[j][k]==-1)dis[j][k]=dis[j][i]+dis[i][k];
									else dis[j][k]=min(dis[j][k],dis[j][i]+dis[i][k]);
								}
						}
				}
				for(ll i=1;i<=n;i++)
				{
					for(ll j=1;j<=n;j++)
					{
						if(dis[i][j]!=-1)
						{
							double tt=(double)dis[i][j];
							if(dis[i][j]>d[i])
							{
								t[i][j]=-1.0;
								continue;
							}
							tt/=v[i];
							t[i][j]=tt;
						}
						else t[i][j]=-1.0;
					}
				}
				for(ll i=1;i<=n;i++)
				{
					for(ll j=1;j<=n;j++)
						for(ll k=1;k<=n;k++)
						{
							if(t[j][i]!=-1.0&&t[i][k]!=-1.0)
								{
									if(t[j][k]==-1.0)t[j][k]=t[j][i]+t[i][k];
									else t[j][k]=min(t[j][k],t[j][i]+t[i][k]);
								}
						}
				}
				//cout<<q<<endl;
	for(ll i=0;i<q;i++)
	{
		ll a,b;
		cin>>a>>b;
		//cout<<a<<b<<endl;
		printf("%.10f%c",t[a][b]," \n"[i==(q-1)]);
	}
	}
	//while(1);
	return 0;
}