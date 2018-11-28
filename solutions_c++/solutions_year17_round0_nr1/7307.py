#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>

int main()
{
	int T,R,K;
	char S[1001];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		R=0;
		bool flag=true;
		scanf("%s %d",S,&K);
		int len=strlen(S);
		for(int j=0;j<len;j++)
		{
			if(S[j]=='-')
			{
				if (K+j>len)
				{
					printf("Case #%d: IMPOSSIBLE\n",i+1);
					flag=!flag;
					break;
				}
				for(int k=j;k<K+j;k++)
					S[k]=(S[k]=='-'?'+':'-');
				R++;
			}
		}
		if(flag)
			printf("Case #%d: %d\n",i+1,R);
		flag=!flag;
	}
	return 0;
}