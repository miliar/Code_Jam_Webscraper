#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		char str[1500];
		int k;
		scanf("%s%d",str,&k);
		int l=strlen(str);
		int ans=0;
		for(int i=0;i<l;i++)
		{
			if(str[i]=='-')
			{
				if(l<(i+k))
				{
					ans=-1;
					break;
				}
				for(int j=i;j<(i+k);j++)
				{
					if(str[j]=='+')
						str[j]='-';
					else
						str[j]='+';
				}
				ans++;
			}
		}
		if (ans==-1)
			printf("Case #%d: IMPOSSIBLE\n",t);
		else
			printf("Case #%d: %d\n",t,ans);
	}
}