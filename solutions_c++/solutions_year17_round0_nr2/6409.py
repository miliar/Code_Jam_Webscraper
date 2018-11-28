#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
	ll t;
	// ifstream inputs;
	// ofstream outputs;
	// inputs.open("B-large.in");
	// outputs.open("output-small-B-large.txt");
	cin>>t;
	// inputs>>t;
	ll op=0;
	while(t--)
	{
		op++;
		string ss;
		cin>>ss;
		// inputs>>ss;
		string ok = ss;
		ll n = ss.length();

		if(n == 1)
		{
			cout<<"Case #"<<op<<": "<<ss<<endl;
			// outputs<<"Case #"<<op<<": "<<ss<<endl;
			continue;
		}
		if(n >= 1)
		{
			for(ll i=ss.length()-1;i>0;i--)
			{
				if(ss[i] < ss[i-1])
				{
					for(ll j=i;j<n;j++)
					{
						if(ss[j]!='9')
							ss[j]='9';
					}
					if(ss[i-1]!='0')
					{
						ss[i-1]-=1;
					}
					else
					{
						ll pp=0;
						for(ll j=i-1;j>=0 and ss[j]!='0';j--)
						{
							pp=j;
							if(ss[j]=='0')
								ss[j]='9';
						}
						ss[pp-1]-=1;
					}
				}
			}
			if(ss[0] == '0')
			{
				string ok="";
				ll pp=0;
				for(ll i=0;i<n and ss[i]!='0';i++)
				{
					pp=i;
				}
				for(ll i=pp+1;i<n;i++)
					ok+=ss[i];
				ss=ok;
			}
			// cout<<ss<<endl;
			cout<<"Case #"<<op<<": "<<ss<<endl;
			// outputs<<"Case #"<<op<<": "<<ss<<endl;
		}
	}
}