#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int y = 1;
	while(t-->0)
	{

		string s; int n;
		int c = 0;
		cin>>s>>n;
		int l = s.size();
		int a[l];

		
		int i,j;
		for(i=0;i<l;i++) if(s[i]=='+') a[i] = 1; else a[i] = 0;

		
		for(i=0;i<=l-n;i++)
		{
			if(a[i]==0)
			{
				for(j=i;j<i+n;j++)
				{
					a[j] = 1-a[j];
				}
				c++;
			}
		}

		for(i=0;i<l;i++) if(a[i]==0) break;
		if(i<l) cout<<"Case #"<<y<<": "<<"IMPOSSIBLE"<<"\n";
		else cout<<"Case #"<<y<<": "<<c<<"\n";
		y++;
	}
	return 0;
}