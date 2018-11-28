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
char swapp(char c)
{
	if(c=='+') 
		return '-';
	else
		return '+';
}
ll process(str a,ll k)
{
	ll i,j,ans=0;
	fwd(i,0,a.size()-k+1)
	{
		if(a[i]=='-')
		{
			ans++;
			fwd(j,i,i+k)
			{
				a[j]=swapp(a[j]);
			}
		}
	}
	fwd(i,0,a.size())
		if(a[i]=='-')
			return -1;
	return ans;
}
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
		cin>>a>>k;
		cout<<"Case #"<<tt<<": ";
		ll ans=0;
		ans=process(a,k);
		if(ans==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;	
}
