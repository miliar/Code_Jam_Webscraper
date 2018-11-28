#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string to_str(ll n)
{
	stringstream ss;
	ss << n;
	string str = ss.str();
	return str;
}

int main()
{
	ll t;
	cin>>t;
	for(ll it=1;it<=t;it++)
	{
		ll n;
		cin>>n;
		string str=to_str(n);
		cout<<"Case #"<<it<<": ";
		for(ll i=0;i<str.length()-1;i++)
		{
			if(str[i]>str[i+1])
			{
				if(i==0)
				{
					str[i]--;
					for(ll j=i+1;j<str.length();j++)
						str[j]='9';
					break;
				}
				else if(str[i]>str[i-1])
				{
					str[i]--;
					for(ll j=i+1;j<str.length();j++)
						str[j]='9';
					break;
				}
				else
				{
					for(ll j=i+1;j<str.length();j++)
						str[j]='9';
					ll j=i-1,count=0;
					char num=str[i];
					while(str[j]==num)
					{
						count++;
						j--;
					}
					j++;
					str[j]--;
					for(ll k=j+1;k<=count;k++)
						str[k]='9';
				}
			}
		}
		for(ll i=0;i<str.length();i++)
			{
				if(str[i]=='0' && i==0)
					;
				else
					cout<<str[i];
			}
		cout<<endl;
}
	return 0;
}

