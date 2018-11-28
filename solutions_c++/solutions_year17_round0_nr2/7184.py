#include<bits/stdc++.h>
#define ll long long int
using namespace std;
string str;
string s;
void game()
{
	ll i=str.length()-2;
	while(i>=0)
	{
		if(str[i]>str[i+1])
		{
			str[i]=str[i]-1;
			for(ll j=i+1;j<str.length();j++)
			{
				str[j]='9';
			}
		}
		i--;
	}
}
int main()
{
	freopen("inpl2.in","r",stdin);
    freopen("outl2.in","w",stdout);
	ios::sync_with_stdio(false);
	ll t,te=1;
	cin>>t;
	while(te<=t)
	{
		ll ans=0,k,n;
		str.clear();
		s.clear();
		cin>>str;
		game();
		for(ll i=0;i<str.length();i++)
		{
			if(str[i]!='0')
			{
				s+=str[i];
			}
		}
		cout<<"Case #"<<te<<": "<<s<<"\n";
		te++;
	}
}
