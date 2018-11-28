#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("g.txt","w",stdout);
	int t,k,p=0;
	cin>>t;
	while(t--)
	{
		
		int flag=0;
		string s;
		cin>>s>>k;
		int ans=0;
		for(int i=0;i<=s.size()-k;i++)
		{
			if(s[i]=='-')
			{
	//			s[i]='+';
				ans++;
				for(int j=i;j<i+k;j++)
				{
					
					if(s[j]=='+')
					s[j]='-';
				//	if(s[j]=='-')
				else
					s[j]='+';
				}
			}
		}
		for(int i=0;i<s.size();i++)
		{
	//		cout<<s[i]<<" ";
			if(s[i]=='-')
			{
				flag++;
			}
		}
		p++;
		if(flag)
		cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<p<<": "<<ans<<endl;
		
	}
}
