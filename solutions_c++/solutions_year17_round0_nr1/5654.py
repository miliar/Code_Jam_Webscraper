#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int cas=1;
	while(t--)
	{
		string s;
		int k;
		cin>>s;
		cin>>k;
		int ans=0;
		for(int i=0;i<s.size()-k+1;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
			}
		}
		bool check=true;
		for(int i=s.size()-1;i>=0 && check;i--)
		{
			if(s[i]=='-')
			{
				cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
				check=false;
			}
		}
		if(check)
		{
			cout<<"Case #"<<cas<<": "<<ans<<endl;
		}
		cas++;
	}
}
