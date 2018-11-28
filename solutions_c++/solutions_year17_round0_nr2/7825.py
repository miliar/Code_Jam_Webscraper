/*input
1
223311
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
		string s,s2;
		ll loc=-1;
		cin>>s;
		s2=s;
		for(ll i=s.length()-1; i>0; i--)
			if(s[i]<s[i-1])
			{
				loc=i-1;
				for(ll j=i; j<s.length(); j++)
					s2[j]='9';
			}
		while(loc-1>=0 && s2[loc]==s2[loc-1])
			s2[loc--]='9';
		if(loc>=0)
			s2[loc]--;
		if(s2[0]=='0')
			s2.erase(0,1);
		cout<<"Case #"<<z<<": "<<s2;
		cout<<endl;
	}
}
// 0 0 0 1
// 9 9 9 1