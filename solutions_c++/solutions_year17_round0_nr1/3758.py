#include <bits/stdc++.h>
#define ll long long 
#define m 1000000007
using namespace std;

int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	ll t,i,j,k,y=1;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>s>>k;
		
		ll n=s.length(),c=0,f=0;
		for(i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				if(i+k<=n)
				{ 
					c++;
					for(j=i;j<=i+k-1;j++)
					{
						if(s[j]=='+')
						s[j]='-';
						else
						s[j]='+';
					}
				}
				else
				{
					f=1;
					break;
				}
			}
		}
	//	cout<<s<<endl;
		cout<<"Case #"<<y<<": ";
		if(f)
		cout<<"IMPOSSIBLE"<<endl;
		else
		cout<<c<<endl;
		y++;
	}
	

	
	return 0;
}
