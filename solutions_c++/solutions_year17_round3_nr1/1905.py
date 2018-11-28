#include<bits/stdc++.h>
using namespace std;
#define fwd(i,a,b) for(i=a;i<b;i++)
#define rev(i,a,b) for(i=a;i>b;i--)
#define ll long long 
#define vll vector< long long > 
#define vi vector<int> 
#define pb push_back
#define pii pair<int,int> 
#define pll pair< ll , ll >
#define F first
#define S second
#define dbl long double
#define str string
#define all(v) v.begin(),v.end()
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
#define M_PI 3.14159265358979323846
#define MOD 1000000007
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll n,i,j,q,r,g,m,e,h,tt,s,l,z,x,y,x1,y1,k,t,p;
	dbl sg,fg,d,sig,nd;
	str a,b,c;
	cin>>t;
	fwd(tt,1,t+1)
	{
		cin>>n>>k;
		cout<<"Case #"<<tt<<": ";
		vector<pll> vv(n+1);
		fwd(i,1,n+1)
		{
			cin>>vv[i].F>>vv[i].S;
		}
		sort(all(vv));
		vector<vector< pair<dbl,ll > > > v(n+1,vector< pair<dbl,ll > >  (k+1,{0.0,0}));
		fwd(i,1,n+1)
		{
			fwd(j,1,k+1)
			{
				if(j>n)
					break;
				if(j!=k)
					sg=v[i-1][j-1].F+2*(dbl)vv[i].F*(dbl)vv[i].S;
				else
					sg=v[i-1][j-1].F+(dbl)vv[i].F*(dbl)vv[i].F+2*(dbl)vv[i].F*(dbl)vv[i].S;
				fg=v[i-1][j].F;
				if(sg>fg)
				{
					v[i][j]={sg,vv[i].F};
				}
				else
					v[i][j]=v[i-1][j];
			}
		}
		// fwd(i,1,n+1)
		// {
		// 	fwd(j,1,k+1)
		// 	{
		// 		cout<<setprecision(9)<<fixed<<v[i][j].F<<" ";
		// 	}
		// 	cout<<endl;
		// }
		cout<<setprecision(9)<<fixed<<(dbl)M_PI*v[n][k].F<<endl;
	}
}