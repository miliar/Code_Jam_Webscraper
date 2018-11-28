#include<bits/stdc++.h>
using namespace std;
#define sf scanf
#define pf printf
#define ll long long int
int main()
{
ll T,k,i,j,u;
sf("%lld",&T);
for(u=1;u<=T;u++)
{
	string s;
	cin>>s;
	ll k,count=0,f=0;
sf("%lld",&k);
for(i=0;i<s.length()-k+1;i++)
{
	if(s[i]=='-')
	{
		for(j=i;j<i+k;j++)
		{
			if(s[j]=='-')
				s[j]='+';
			else
				s[j]='-';
	}count++;
}}
for(i=0;i<s.length();i++)
{
if(s[i]=='-')
f=1;}
if(f!=1)
{
pf("Case #%lld: %lld\n",u,count);}
else
pf("Case #%lld: IMPOSSIBLE\n",u);
}}
