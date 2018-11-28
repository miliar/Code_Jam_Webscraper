#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define LL long long
using namespace std;
int T;
inline void open()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
}
char s[20];
int main()
{
	open();
	scanf("%d",&T);int cas=0;
	while(T--)
	{
		scanf("%s",s);
		int len=strlen(s);bool tag=0;
		for(int i=1;i<len;i++)
		{
			if(s[i]>=s[i-1]) continue;
			else tag=1;
		}
		if(!tag)
		{
			printf("Case #%d: %s\n",++cas,s);
			continue;
		}
		LL MAXN=0;
		for(int i=0;i<len;i++)
		{
			if(s[i]>'0')
			{
				s[i]--;bool p=0;
				LL tmp=int(s[0]-'0');
				for(int j=1;j<=i;j++)
				{
					if(s[j]<s[j-1]) p=1;
					tmp*=10;tmp+=int(s[j]-'0');
				}
				if(p) break;
				for(int j=i+1;j<len;j++)
				{
					tmp*=10;tmp+=9;
				}
				MAXN=max(MAXN,tmp);
				s[i]++;
			}
		}
		printf("Case #%d: %lld\n",++cas,MAXN);
	}
	return 0;
}
