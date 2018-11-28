#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	char str[1001];
	int T,k,i,cas,l,j,ans;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%s%d",str,&k);
		l=strlen(str);
		replace(str,str+l,'+',(char)1);
		replace(str,str+l,'-',(char)0);
		
		ans=0;
		for(i=0;i<=l-k;++i)
		{
			if(!str[i])
			{
				for(j=0;j<k;++j)
				{
					str[i+j]^=1;
				}
				++ans;
			}
		}
		printf("Case #%d: ",cas);
		if(count(str+l-k,str+l,0))
		{
			puts("IMPOSSIBLE");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
	return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/

