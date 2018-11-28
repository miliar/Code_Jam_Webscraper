/*
Shubham Gupta
=============

MNNIT CSE 3rd year
==================
*/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
ll n,k,x,y,z,c;
int main()
{
ll t;
scanf("%lld",&t);
for(ll i=1;i<=t;i++){
	map<ll,ll> shu;
	scanf("%lld %lld",&n,&k);
	shu[n]=1;
	for(ll j=1;j<=k;)
	{
		x=shu.rbegin()->first;
		c=shu.rbegin()->second;
		shu.erase(x);
		y=x/2;
		z=x-y-1;
		//printf("%lld %lld %lld\n",j,x,c);
		if(shu.find(y)==shu.end())
			shu[y]=0;
		if(shu.find(z)==shu.end())
			shu[z]=0;
		shu[y]+=c;
		shu[z]+=c;
		j+=c;
	}
	printf("Case #%lld: %lld %lld\n",i,y,z);
}
return 0;
}