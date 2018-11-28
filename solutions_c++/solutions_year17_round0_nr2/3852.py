#include<stdio.h>
#include<cmath>
#include<algorithm>
#include<string.h>
using namespace std;

int k;
char s[30];
int l;
int a[30];

int dfs(int pos,int num,int o)
{
	if(pos==l)
	{
		int flag=0;
		for(int i=0;i<l;i++)
		{
			if(flag==0&&a[i]==0)
			{
				continue;
			}
			else flag=1;
			printf("%d",a[i]);
		}
		return 1;
	}
	for(int i=9;i>=num;i--)
	{
		if(o)
		{
			if(i>s[pos]-'0')continue;
		}
		a[pos]=i;
		if(dfs(pos+1,i,o&&(i==s[pos]-'0'?1:0)))return 1;
	}
	return 0;
}

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
		scanf("%s",s);
		l=strlen(s);
		for(int i=s[0]-'0';i>=0;i--)
		{
			a[0]=i;
			if(dfs(1,i,i==s[0]-'0'?1:0))break;
		}
		printf("\n");
	}
	return 0;
}
