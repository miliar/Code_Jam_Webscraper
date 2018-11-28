#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int T,k;
char S[10000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%s",S);
		scanf("%d",&k);
		int len=strlen(S);
		int ans=0;
		for (int i=0;i<=len-k;i++)
		if (S[i]=='-')
		{
			++ans;
			for (int j=i;j<i+k;j++) S[j]=(S[j]=='+')?'-':'+';
		}
		bool flag=true;
		for (int i=len-k;i<len;i++) if (S[i]=='-') flag=false;
		printf("Case #%d: ",cas);
		if (!flag) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}	
} 
