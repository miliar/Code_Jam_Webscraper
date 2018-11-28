#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 100005
using namespace std;
bool a[100000],b[100000];
char s[100000];
int len;
int main()
{
	freopen("A-large.in", "r", stdin);  
    freopen("sample1-l.out", "w", stdout);  
	int i,j,k,t,tt=0,sum,ans;
	scanf("%d",&t);
	while(t--)
	{
		tt++;
		scanf("%s",s);
		scanf("%d",&k);
		len=strlen(s); 
		memset(b,0,sizeof(bool)*(len+1));
		for(i=0;i<len;i++)
		{
			if(s[i]=='+')
			{
				a[i]=0;
			}
			else
			{
				a[i]=1;
			}
		}
		sum=ans=0;
		for(i=0;i<=len-k;i++)
		{
			if((a[i]+sum)%2)
			{
				ans++;
				b[i]=1;
				sum++;
			}
			if(i-k+1>=0)
			{
				sum-=b[i-k+1];
			}
		}
		int fg=0;
		for(i=len-k+1;i<len;i++)
		{
			if((sum+a[i])%2!=0)
			{
				fg=1;
				break;
			}
			if(i-k+1>=0)
			{
				sum-=b[i-k+1];
			}	
		}
		printf("Case #%d: ",tt);
		if(fg)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
}
