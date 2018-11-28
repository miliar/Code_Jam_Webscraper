#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cstdlib>
using namespace std;
char s[1000+10];
int num[1000+10];
int ans[1000+10];
bool dfs(int dep,int now,bool low)
{
	if(dep==-1)return true;
	for(int i=low?9:num[dep];i>=now;i--)
	{
		ans[dep]=i;
		if(dfs(dep-1,i,low||i<num[dep]))return true;
	}
	return false;
}
int main()
{
	int T;
	scanf("%d",&T);
	int cas=0;
	while(T--)
	{
		printf("Case #%d: ",++cas);
		scanf("%s",s);
		int len=strlen(s);
		reverse(s,s+len);
		for(int i=0;i<len;i++)num[i]=s[i]-'0';
		if(dfs(len-1,1,false))
		{
			for(int i=len-1;i>=0;i--)printf("%d",ans[i]);
		}
		else
		{
			for(int i=len-2;i>=0;i--)printf("9");
		}
		printf("\n");
	}
	return 0;
}