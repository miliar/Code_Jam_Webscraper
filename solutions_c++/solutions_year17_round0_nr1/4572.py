#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=0;
		for(int i=0;i+k<=s.length();i++)
		{
			if(s[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				ans++;
			}	
		}
		int flag=0;
		for(int i=0;i<s.length();i++)
			if(s[i]=='-')
				flag=1;
		if(flag)
			printf("Case #%d: IMPOSSIBLE\n",cnt);
		else
			printf("Case #%d: %d\n",cnt,ans);
	}
	return 0;
}