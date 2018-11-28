#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
ll t,k,i,j,u;
cin>>t;
for(u=1;u<=t;u++)
{
	string s;
	cin>>s;
	ll k,c=0,f=0;
cin>>k;
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
	}c++;
}}

for(i=0;i<s.length();i++)
{
if(s[i]=='-')
f=1;}
if(f!=1)
{
cout<<"Case #"<<u<<": "<<c<<"\n";}
else
cout<<"Case #"<<u<<": "<<"IMPOSSIBLE"<<"\n";}}
