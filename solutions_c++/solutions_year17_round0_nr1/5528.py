#include<cstring>
#include<cstdio>
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=1;
	scanf("%d",&T);
	while(T--)
	{
		char in[1005];
		int k,c=0;
		scanf("%s %d",in,&k);
		int len=strlen(in);
		bool happy=1;
		for(int i=0;i<len;i++)
		{
			if(i+k>len&&in[i]=='-')
			{
				printf("Case #%d: IMPOSSIBLE\n",cas);
				happy=0;
				break;
			}
			if(i+k<=len&&in[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(in[j]=='+') in[j]='-';
					else in[j]='+';
				}
				c++;
			}
		}
		if(happy) printf("Case #%d: %d\n",cas,c);
		cas++;
	}
}
