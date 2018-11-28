#include <cstdio>
#include <string.h>

using namespace std;
const int maxn=1000;

char s[maxn+5];
int k;
int f[maxn+5];

int solve()
{
	memset(f,0,sizeof(f));
	int cnt=0;
	int cur=0;
	
	int len=strlen(s+1);
	int res=0;
	for (int i=1;i<=len;++i)
	{
		cur=(s[i]=='+')? 1:0;
		if (((cur+cnt)%2)==0)
		{
			//printf("i=%d\n",i);
			if (i+k-1>len) return -1;
			else
			{
				f[i]=1;
				++res;
			}
		}
		cnt+=f[i];
		if (i-k+1>0) cnt-=f[i-k+1];
	}
	return res;
}

int main(void)
{
	#ifdef ex
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt","w",stdout);
	#endif
	
	int T;
	scanf("%d",&T);
	
	for (int Case=1;Case<=T;++Case)
	{
		scanf("%s%d",s+1,&k);
		int ans=solve();
		if (ans==-1) printf("Case #%d: IMPOSSIBLE\n",Case);
		else printf("Case #%d: %d\n",Case,ans);
	}
}
