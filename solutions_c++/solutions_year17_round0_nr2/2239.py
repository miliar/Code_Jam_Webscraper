#include<bits/stdc++.h>

using namespace std;

int T;
char S[10000];

int main()
{
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%s",S);
		int len=strlen(S);
		int mm=S[0]-'0';
		int nn=0;
		bool flag=true;
		for (int i=1;i<len;i++)
		if (S[i]!=S[i-1])
		{
			if (S[i]-'0'<mm)
			{
				flag=false;
				break;
			}
			else 
			{
				mm=S[i]-'0';
				nn=i;
			}
		}
		printf("Case #%d: ",cas);
		if (flag) 
		{
			printf("%s\n",S);
			continue;
		}
		S[nn]=S[nn]-1;
		for (int i=nn+1;i<len;i++) S[i]='9';
		flag=true;
		for (int i=0;i<len;i++)
		{
			if (S[i]=='0')
			{
				if (flag) continue;
			}
			else flag=false;
			printf("%c",S[i]);
		}
		puts("");
	}
	return 0;
}
