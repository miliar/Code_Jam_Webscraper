#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("oversized.txt","r",stdin);
    freopen("outputgc.txt","w",stdout);
	int t;
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		char s[1009];
		int k;
		cin>>s>>k;
		int ans=0,len=strlen(s);
		for(int i=0;i<=len-k;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=i;j<i+k;j++)
				{
					//flip(s[i]);
					if(s[j]=='-')
					{
						s[j]='+';
					}
					else
					{
						s[j]='-';
					}
				}
			}
		}
		int flag=0;
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-')
			flag=1;
		}
		if(flag==0)
		{
			cout<<"Case #"<<q<<": "<<ans<<endl;
		}
		else
		{
			cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
		}
	}
}
