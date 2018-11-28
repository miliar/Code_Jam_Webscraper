                                           //shubham arya
		                               //NIT Patna
#include <bits/stdc++.h>
#define ll long long int
#define mp make_pair
#define pi pair<ll,ll>
using namespace std;
const ll MAX=1e13;
const ll MOD=10000002;

int main()
{
	/*std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);*/
	ll i,j,k,n,t,ts;
	cin>>t;
	for(ts=1;ts<=t;ts++)
	{
		char s[25];
		char *p;
		cin>>s;
		n=strlen(s);
		if(n==1)
		cout<<"Case #"<<ts<<": "<<s<<endl;
		else if(n==2)
		{
		if(s[1]<s[0])
		{
            s[1]='9';
			ll x=s[0];
		    s[0]=x-1;
		}
		if(s[0]=='0')
		{
		p=s+1;
		cout<<"Case #"<<ts<<": "<<p<<endl;		
		}
		 else
		 cout<<"Case #"<<ts<<": "<<s<<endl;
		}
		else
		{
			j=0;
		while(j<n-1)
		{
			if(s[j]>s[j+1])
			break;
			j++;
		}
		if(j==n-1)
		cout<<"Case #"<<ts<<": "<<s<<endl;
		else
		{
		for(i=n-1;i>1;i--)
		{
			    s[i]='9';
				if(s[i-1]!='0')
				{
				ll x=s[i-1];
				s[i-1]=x-1;
				}
		}
		if(s[0]=='1' && s[1]=='0')
		{
			s[0]='0';s[1]='9';
		}
		else if(s[1]<s[0])
		{
            s[1]='9';
			ll x=s[0];
		    s[0]=x-1;
		}
		if(s[0]=='0')
		{
			p=s+1;
		cout<<"Case #"<<ts<<": "<<p<<endl;
		}
		else
		cout<<"Case #"<<ts<<": "<<s<<endl;
		}	
		}
	}
	return 0;
}

