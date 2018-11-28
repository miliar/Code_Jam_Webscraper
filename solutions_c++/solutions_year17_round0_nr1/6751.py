#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int main ()
{
	int t;
	scanf("%d",&t);
	for(int ct=1;ct<=t;ct++)
	{
		char str[1009]={};
		int k,len,ans=0;
		scanf("%s",str);
		scanf("%d",&k);
		len = strlen(str);
		for(int i=0;i<len-k+1;i++)
		{
			if(str[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(str[j]=='+')str[j]='-';
					else str[j]='+';
				}
				ans++;
			}
		}
		for(int i=len-k;i<len;i++)
		{
			if(str[i]=='-')
			{
				ans=-1;
				break;
			}
		}
		printf("Case #%d: ",ct);
		if(ans==-1)printf("IMPOSSIBLE");
		else printf("%d",ans);
		if(ct!=t)printf("\n");
	}
	return 0;
}
