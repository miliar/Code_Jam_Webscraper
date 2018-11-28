#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int cn=1;
	while(t--)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int c=0;
		int n=s.size();
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-' && (i+k)<=n)
			{
				s[i]='+';
				c++;
				for(int j=i+1;j<k+i;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		int d=0;
		for(int i=0;i<n;i++)
			if(s[i]=='-')
			{
				d=1;
				cout<<"Case #"<<cn<<": "<<"IMPOSSIBLE"<<"\n";
				cn++;
				break;
			}
		if(d!=1)
		{
			cout<<"Case #"<<cn<<": "<<c<<"\n";
			cn++;
		}
	}
}


