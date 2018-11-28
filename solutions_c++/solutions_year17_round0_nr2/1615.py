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
char str[2000];
int main()
{
ll t;
scanf("%lld",&t);
for(ll i=1;i<=t;i++){
	ll ans=0;
	scanf("%s",str);
	ll n=strlen(str);
	for(ll j=n-1;j>0;j--)
	{
		if(str[j]<str[j-1])
		{
			str[j-1]-=1;
			for(ll k=j;k<n;k++)
				str[k]='9';
		}
		//printf("%s\n",str);
	}
	if(str[0]=='0' && n>1)
		printf("Case #%lld: %s\n",i,str+1);
	else
		printf("Case #%lld: %s\n",i,str);
}
return 0;
}