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
#define vpll vector< pll >
#define F first
#define S second
#define dbl double
#define str string
#define P2 3.14159265358979323846  /* pi */
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
#define MOD 1000000007
#define gc getchar_unlocked 
#define pc putchar_unlocked
str call(str a,ll i)
{
	ll j;
	ll car=0;
	rev(j,i,0)
	{
		if(car==1)
		{
			a[j]-=1;
			if(a[j]+1=='0')
			{
				a[j]='9';
			}
			car=0;
		}
		if(a[j]<a[j-1])
		{
			a[j]='9';
			car=1;
		}
	}
	if(car==1)
	{
		a[j]-=1;
		if(a[j]+1=='0')
		{
			a[j]='9';
		}
		car=0;
	}
	return a;
}
string process(str a)
{
	ll i,j,car=0;
	fwd(i,0,a.size()-1)
	{
		if(a[i]>a[i+1])
		{
			for(j=i+1;j<a.size();j++)
			{
				a[j]='9';
			}
			a[i]-=1;
			return call(a,i);
		}
	}
	return a;
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
		cin>>a;
		b=process(a);
		bool flag=false;
		cout<<"Case #"<<tt<<": ";
		fwd(i,0,a.size())
		{
			if(b[i]!='0')
				flag=true;
			if(flag)
				cout<<b[i];
		}
		cout<<endl;
	}
	return 0;
}	