#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int tt=1;
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		int cnt=0;
		printf("Case #%d: ",tt);
		tt++;
		int n=s.size(),i,j;
		for(i=0;i<=n-k;i++)
		{
			if(s[i]=='-')
			{
				cnt++;
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='+')s[j]='-';
					else if(s[j]=='-')s[j]='+';
				}
			}
		}
		bool f=0;
		for(i=n-k;i<n;i++)
		{
			if(s[i]=='-')
			{
				f=1;break;
			}
		}
		if(f)cout<<"IMPOSSIBLE";
		else cout<<cnt;
		printf("\n");
	}
	return 0;
}