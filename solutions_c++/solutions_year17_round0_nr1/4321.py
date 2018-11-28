#include<bits/stdc++.h>
using namespace std;
const int MAXN=1005;
char s[MAXN];
int sv[MAXN];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		int len,k;
		scanf("%s%d",s+1,&k);
		len=strlen(s+1);
		for(int i=1;i<=len;i++)
		{
			sv[i]=(s[i]=='+'?1:0);
		}
		int ans=0;
		for(int i=1;i<=len-k+1;i++)
		{
			if(sv[i])
				continue;
			else
			{
				ans++;
				for(int j=i;j<i+k;j++)
				{
					sv[j]^=1;
				}
			}
		}
		for(int i=1;i<=len;i++)
		{
			if(!sv[i])
			{
				ans=-1;
				break;
			}
		}
		printf("Case #%d: ",_);
		if(ans==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
