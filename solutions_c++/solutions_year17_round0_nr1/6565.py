#include <stdio.h>
#include <string.h>
void solve(int T);
int main()
{
	freopen("largeA.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) solve(i);
}
char x[1010];
void solve(int T)
{
	int a,b;
	int s = 0;
	scanf("%s%d",x+1,&a);
	b = strlen(x+1);
	for(int i=1;i<=b-a+1;i++)
	{
		if(x[i]=='-')
		{
			for(int j=i;j<=i+a-1;j++)
			{
				x[j] = '+'+'-'-x[j];
			}
			s++;
		}
	}
	for(int i=b-a+2;i<=b;i++)
	{
		if(x[i]=='-')
		{
			printf("Case #%d: IMPOSSIBLE\n",T);
			return;
		}
	}
	printf("Case #%d: %d\n",T,s);
}
