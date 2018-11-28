#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%lld",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
ll x,y;
void f(ll n,ll m)
{
	if(m==1)
	{
		x=n/2;
		y=(n-1)/2;
		return;
	}
	n--;
	m--;
	if(m%2)
		f((n+1)/2,(m+1)/2);
	else
		f(n/2,m/2);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   	ll t,n,m,i;
   	sd(t);
   	for(i=1;i<=t;i++)
   	{
   		sd(n);
   		sd(m);
   		f(n,m);
   		printf("Case #%lld: %lld %lld\n",i,x,y);
   	}
    return 0;
}