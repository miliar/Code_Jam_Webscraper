#include<bits/stdc++.h>

#define ll long long 
using namespace std;



int main()
{
	int t, it;
	cin>>t;
	for(it=1; it<=t; it++)
	{
		cout<<"Case #"<<it<<": ";
		string s;
		int i, j, n, z;
		cin>>s;
		n=s.length();
		z=n; 
		for(i=0; i<n-1; i++)
		{
			if(s[i]>s[i+1])
			{
				j=i;
				while(s[j]==s[i] && j>=0)
				{
					j--;
				}
				j++;

				s[j]=s[j]-1;

				z=j+1;
				break;

			}
		}

		for(i=z; i<n; i++)
			s[i]='9';

		ll ans=0, mul=1;

		for(i=n-1; i>=0; i--)
		{
			ans=ans+((s[i]-'0')*mul);
			mul=mul*10;
		}

		cout<<ans<<endl;

	}
}