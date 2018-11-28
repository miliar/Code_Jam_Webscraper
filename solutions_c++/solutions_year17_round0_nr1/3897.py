#include<stdio.h>
#include<cmath>
#include<algorithm>
#include<string.h>
using namespace std;

int k;
char s[1010];

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
		printf("Case #%d: ",cas++);
		int ans=0;
		scanf("%s%d",s,&k);
		int l=strlen(s);
		for(int i=0;i<l-k+1;i++)
		{
			if(s[i]=='-')
			{
				for(int j=i;j<=i+k-1;j++)
				{
					if(s[j]=='+')s[j]='-';
					else s[j]='+';
				}
				ans++;
			}
		}
		int flag=0;
		for(int i=l-k+1;i<l;i++)
		{
			if(s[i]=='-')
			{
				flag=1;
			}
		}
		if(flag)printf("IMPOSSIBLE\n");
		else
		{
			printf("%d\n",ans);
		}
	}
	return 0;
}
