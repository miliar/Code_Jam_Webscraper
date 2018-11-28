#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <set>
#define LL long long
#define N 100005
#define INF 0x7fffffff
using namespace std;
char inp[1005];
int T,cnt,flag,n;
int len;
void change(int x,int y)
{
	for(int i=x;i<x+y;i++)
	{
		if(inp[i]=='+')inp[i]='-';
		else inp[i]='+';
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large1.out","w",stdout);
	scanf("%d",&T);
	for(int case1=1;case1<=T;case1++)
	{
		cnt=0;flag=1;
		scanf("%s",inp);
		scanf("%d",&n);
		len=strlen(inp);
		for(int i=0;i<len;i++)
		{
			if(inp[i]=='-'&&i<=len-n)
				{
					//printf("%d\n",i);
					change(i,n);
					cnt++;
				}
			if(i>len-n&&inp[i]=='-')
			{
				//for(int j=0;j<len;j++)printf("%c ",inp[i]);
				//printf("\n");
				printf("Case #%d: IMPOSSIBLE\n",case1);
				flag=0;
				break;
			}
		}
		if(flag)printf("Case #%d: %d\n",case1,cnt);
	}
	return 0;
}
