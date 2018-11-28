#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Output.out","w",stdout);
	int t,k,count,caseno=1;
	bool check;
	string s;
	scanf("%d",&t);
	while(t--)
	{
		count=0;
		cin>>s;
		scanf("%d",&k);
		for(int i=0;i<=s.length()-k;i++)
		{
			if(s[i]=='-')
			{
				count++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
			//cout<<s<<'\n';
		}
		check=1;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				check=0;
				break;
			}
		}
		printf("Case #%d: ",caseno);
		if(check) printf("%d",count); else printf("IMPOSSIBLE");
		printf("\n");
		caseno++;
	}
	return 0;
}
