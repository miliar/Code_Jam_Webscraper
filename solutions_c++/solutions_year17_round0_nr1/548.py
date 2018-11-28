#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
char s[1010];
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{	int K,i,len;
		scanf("%s",s+1); cin>>K;
		len=strlen(s+1);
		int cnt=0;
		for(i=1;i+K-1<=len;i++) if(s[i]=='-')
		{	cnt++;
			for(int j=1;j<=K;j++) s[i+j-1]=(s[i+j-1]=='+'?'-':'+');
		}
		int flag=0;
		for(i=i;i<=len;i++) if(s[i]=='-'){flag=1; break;}
		if(flag) printf("Case #%d: IMPOSSIBLE\n",casi);
		else printf("Case #%d: %d\n",casi,cnt);
	}
	return 0;
}

