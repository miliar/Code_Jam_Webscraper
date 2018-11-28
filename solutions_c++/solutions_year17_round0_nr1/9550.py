#include<cstdio>
#include<cstring>
char s[1010];
int len,k,ans;
void check()
{
	for(int i=1;i<=len;++i)
		if(s[i]=='-')
		{
			if(i+k-1>len)
			{
				puts("IMPOSSIBLE");
				return;
			}
			++ans;
			for(int j=0;j<k;++j)
				if(s[i+j]=='+')
					s[i+j]='-';
				else
					s[i+j]='+';
		}
	printf("%d\n",ans);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		scanf("%s%d",s+1,&k);
		len=strlen(s+1);
		ans=0;
		printf("Case #%d: ",i);
		check();
	}
	return 0;
} 
