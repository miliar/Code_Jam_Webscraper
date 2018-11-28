#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inp.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n;
	cin>>t;
	string s;
	for (int Case = 1; Case <= t; Case++)
	{
		cin>>s>>n;
		int len=s.length();
		int flag=1,ans=0;
		for(int start=0;start<len;start++)
		{
			if(s[start]=='-')
			{
				if(len-start<n)
				{
					flag=0;
					break;
				}
				else
				{
					for(int i=0;i<n;i++)
					{
						s[start+i]=(s[start+i]=='-')?'+':'-';
					}
					ans++;
				}
			}

		}
		if(!flag)
		{
			cout<<"Case #"<<Case<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else
			cout<<"Case #"<<Case<<": "<<ans<<"\n";
	}	

}