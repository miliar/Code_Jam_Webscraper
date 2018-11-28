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
#define f first
#define s second
#define dbl double
#define str string
#define all(v) v.begin(),v.end()
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
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
		cout<<"Case #"<<tt<<": ";
		cin>>d>>n;
		sg=0;
		fwd(i,0,n)
		{
			cin>>k>>x;
			sg=max(sg,((dbl)(d-k)/(dbl)x));
		}
		cout<<setprecision(9)<<fixed<<(dbl)d/sg<<endl;
	}
	return 0;	
}
