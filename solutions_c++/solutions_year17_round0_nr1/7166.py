#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<b;++i)
#define mod 1000000007
#define rev(i,a,b) for(i=a;i>b;--i)
#define ll long long int
#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sstr(x) scanf("%s",x)
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vll vector<ll>
#define mapii map<int, int>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define ins(x) insert(x)
#define mulmap multimap<int, int>
#define itr ::iterator
ll pow(ll, ll);
ll max(ll, ll);
ll min(ll, ll);
using namespace std;
int main()
{
	int t,cases,count,k,len,i,j,flag;
	char x[1005];
	si(t);
	cases=1;
	while(t--)
	{
		count=0;
		sstr(x);
		si(k);
		len = strlen(x);
		rep(i,0,len-k+1)
		{
			if(x[i]=='-')
			{
				count++;
				rep(j,i,i+k)
				{
					if(x[j]=='+')
						x[j]='-';
					else
						x[j]='+';
				}
			}
		}
		flag=0;
		rep(i,0,len)
		{
			if(x[i]=='-')
				flag=1;
		}
		if(flag==0)
			cout<<"Case #"<<cases<<": "<<count<<endl;
		else
			cout<<"Case #"<<cases<<": IMPOSSIBLE"<<endl;
		cases++;
	}
	return 0;
}
ll max(ll a, ll b)
{
	if(a>b)
		return a;
	else
		return b;
}
ll min(ll a, ll b)
{
	if(a>b)
		return b;
	else
		return a;
}
ll pow(ll a, ll b)
{
	ll ans=1;
	while(b)
	{
		if(b&1)
		{
			ans=ans*a;
		}
		a=a*a;
		b=b>>1;
	}
	return ans;
}
