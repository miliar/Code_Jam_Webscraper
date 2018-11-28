#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int num[20],mi[20];
int ans[20];
bool flag;
int len;
void dfs(int i,int la,bool up)
{
	if(i==-1)
	{
		flag=false;
		return ;
	}
	int lim=up?num[i]:9;
	for(int j=lim;j>=0&&flag;j--)
	{
		if(j>=la)
		{
			ans[i]=j;
			dfs(i-1,j,up&&j==num[i]);
		}
	}
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		ll n;
		len=0;
		scanf("%lld",&n);
		while(n)
		{
			num[len++]=n%10;
			n/=10;
		}
		printf("Case #%d: ",_);
		flag=true;
		dfs(len-1,0,true);
		bool zero=false;
		for(int i=len-1;i>=0;i--)
		{
			if(!ans[i]&&!zero)
				continue;
			zero=true;
			printf("%d",ans[i]);
		}
		printf("\n");
	}
	return 0;
}
