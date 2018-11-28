#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
	// your code goes here
	
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t, it;
	cin>>t;
	for(it=1; it<=t; it++)
	{
		string s;
		int k;
		cin>>s>>k;
		int c=0;
		int i, j, n=s.size();
		for(i=0; i<=n-k; i++)
		{
			if(s[i]=='-' and (i+k)<=n)
			{
				c++;
				for(j=i; j<i+k; j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}

		for(i=0; i<n; i++)
		{
			if(s[i]=='-')
			{
				cout<<"Case #"<<it<<": "<<"IMPOSSIBLE\n";
				break;
			}
		}
		if(i==n)
			cout<<"Case #"<<it<<": "<<c<<"\n";
	}
	
	return 0;
}
