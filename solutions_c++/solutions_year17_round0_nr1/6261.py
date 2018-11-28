#include <iostream>
#include <string>
#define ll long long
using namespace std;

int main() 
{
	ll  c,k,i;
	cin>>c;
	for(ll m=1;m<=c;m++)
	{
		
	ll f=0,count=0;
	string s;
	cin>>s>>k;
	for(ll i=0;i<=s.size()-(k);i++)
	{ 	
		ll t=k;
		ll j=i;
		if(s[j]=='-')
		{ 
			count++;
			while(t--)
			{
			   if(s[j]=='-')
			   s[j]='+';
			   else
			   s[j]='-';
			   
			   j++;
			}
		}
	}
	for(ll q=i;q<s.size();q++)
	{
		if(s[q]=='-')
		{
			f=1;
			cout<<"Case #"<<m<<": IMPOSSIBLE"<<endl;
			break;
		}
	}
	if(f==0)
	cout<<"Case #"<<m<<": "<<count<<endl;
	
	}
	return 0;
}