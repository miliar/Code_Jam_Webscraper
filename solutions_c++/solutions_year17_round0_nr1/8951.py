#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define LL long long
using namespace std;
int T;
inline void open()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
}
char s[1005];
int main()
{
	int cas=0;
	open();
	scanf("%d",&T);
	while(T--)
	{
		//getchar();
		scanf("%s",s);int cnt;
		scanf("%d",&cnt);
		int len=strlen(s);bool tag=0;
		bool flag=0;int coun=0;
		while(1)
		{
			bool p=0;
			for(int i=0;i<len;i++)
			{
				if(s[i]=='-') p=1;
			}
			if(p==0)
			{
				flag=1;break;
			}			
			coun++;
			int pos=-1;
			for(int i=0;i<len;i++)
			{
				if(s[i]=='-')
				{
					pos=i;
					break;
				}
			}
			for(int i=pos;i<=pos+cnt-1;i++)
			{
				if(i>=len)
				{
					tag=1;break;
				}
				char x;
				if(s[i]=='-') x='+';
				if(s[i]=='+') x='-';
				s[i]=x;
			}
			if(tag) break;
		}
		if(tag) printf("Case #%d: IMPOSSIBLE\n",++cas);
		if(flag) printf("Case #%d: %d\n",++cas,coun);
	}
	return 0;
}
