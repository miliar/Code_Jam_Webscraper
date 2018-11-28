#include <bits/stdc++.h>
#define ll long long int
#define ld long double 
#define MOD 1000000007 
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define ff first
#define ss second 
#define ios ios_base::sync_with_stdio(false);

using namespace std;

int main()
{
	ll t;
	string s;
	cin>>t;
	for(ll i=1; i<=t; i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>s;
		ll k=0, val=0;
		for(ll i=0; i<s.length()-1; i++)
		{
			if(s[i]>s[i+1])
			{
				k=i;
				s[i]--;
				val=s[i]+1;
				i++;
				while(i<s.length())
				{
					s[i]='9';
					i++;
				}
			}
		}
		for(ll i=k-1; i>=0; i-- )
		{
			if(s[i]==val)
			{
				s[i+1]='9';
				s[i]--;
			}
			else if(s[i]<val)
			{
				break;
			}
		}
		k=0;
		for(ll i=0;i<s.length(); i++)
		{
			if(s[i]=='0' and k==0)
			{

			}
			else
			{
				k=1;
				cout<<s[i];
			}
		}
		cout<<endl;
	}
	return 0;
}