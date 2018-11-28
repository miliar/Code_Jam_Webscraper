#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	ll t,k,n;
	cin>>t;
	ll p=1;
	ll flag=0;

	while(t--)
	{
		string s;
		cin>>s;
		//cout<<"k"<<endl;

		for(ll i=s.length()-1;i>=1;i--)
		{

			if(s[i-1]>s[i])
			{
				

				s[i-1]--;
				//cout<<s[i-1]<<" "<<s[i]<<endl;
				for(ll j=i;j<s.length();j++)
					s[j]='9';
				
				
			}
		}
		cout<<"Case #"<<p<<": "; 
		for(ll i=0;i<s.length();i++)
			if(s[i]!='0')
			cout<<s[i];
		cout<<endl;	
		p++;		
	}
}
