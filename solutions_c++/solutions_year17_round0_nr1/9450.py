#include<cstdio>
#include<cstring>
#include<algorithm>
#define rep(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

const int maxn=2000;
int n;
int s[maxn+1],i;

void read()
{
	i=0;
	char c;
	do
	{
		c=getchar();
		if(c=='+')s[++i]=1;
		else if(c=='-')s[++i]=0;
		else if(c==' ')
		{
			scanf("%d\n",&n);
			break;
		}
	}while(1);
	return;
}

int work()
{
	read();
	int ans=0;
	rep(j,1,i)
	{
		if(s[j]==0)
		{
			if(j+n-1>i)return -1;
			rep(k,j,j+n-1)s[k]=!s[k];
			ans++;
		}	
	}
	return ans;
}

int main()
{
	freopen("cards.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	rep(i,1,t)
	{
		int k=work();
		if(k==-1)
			printf("Case #%d: IMPOSSIBLE\n",i);
		else printf("Case #%d: %d\n",i,k);
	}
	return 0;
}
