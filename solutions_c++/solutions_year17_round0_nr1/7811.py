/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;
int main()
{
	ios::sync_with_stdio(false);
	ll t;
	cin>>t;
	for(ll z=1; z<=t; z++)
	{
		string s;
		ll k,count=0;
		bool flag=true;
		cin>>s>>k;
		for(ll i=0; i<s.length(); i++)
		{
			if(s[i]=='-')
			{
				count++;
				if(i+k<=s.length())
				for(ll j=0; j<k; j++)
				{
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
			}
		}
		for(ll i=0; i<s.length(); i++)
		if(s[i]=='-')
			flag=false;
		if(flag)
			cout<<"Case #"<<z<<": "<<count<<endl;
		else
			cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;	
	}
}