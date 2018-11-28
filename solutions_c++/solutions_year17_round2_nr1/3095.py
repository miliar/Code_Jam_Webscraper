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
set <string> str;
int main()
{
ll t,d,n,x,y;
scanf("%lld",&t);
for(ll i=1;i<=t;i++)
{
	scanf("%lld %lld",&d,&n);
	double ans=1000000000000000000,tim=0,xx,yy;
	for(int j=0;j<n;j++)
	{
		scanf("%lld %lld",&x,&y);
		xx=x;
		yy=y;
		tim=(d-xx)/yy;
		ans=min(ans,d/tim);
		//printf("%lld %lf\n",d,tim);
	}
	printf("Case #%lld: %lf\n",i,ans);
}
return 0;
}