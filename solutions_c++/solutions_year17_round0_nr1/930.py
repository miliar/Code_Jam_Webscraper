#include <bits/stdc++.h>
#define range(i,c,o) for(register int i=(c);i<(o);++i)
#define dange(i,c,o) for(register int i=(c);i>(o);--i)
using namespace std;

inline void rev(char&c) {c=c=='+'?'-':'+';}

static int T,m; char str[1005];
int main()
{
	scanf("%d",&T);
	range(data,1,T+1)
	{
		scanf("%s%d",str,&m); int n=strlen(str),cnt=0;
		range(i,0,n-m+1) if(str[i]=='-')
		{
			range(j,i,i+m) rev(str[j]); ++cnt;
		}
		bool flag=0;
		range(i,n-m+1,n) if(flag=str[i]=='-') break;
		printf("Case #%d: ",data);
		flag?puts("IMPOSSIBLE"):printf("%d\n",cnt);
	}
	return 0;
}