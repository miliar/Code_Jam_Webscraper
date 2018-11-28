#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;

char s[1005];
int T,K,L,ANS;

void solve()
{
	int i=1,j;
	while (1)
	{
		while (s[i]!='-' && i<L)	++i;
		if (i>L)	break;
		if (i+K-1>L)	break;
		for (j=i;j<=i+K-1;j++)
		{
			if (s[j]=='+')	s[j]='-';
			else	s[j]='+';
		}
		++ANS;
	}
}

void check()
{
	int i;
	bool flag=true;
	for (i=1;i<=L;i++)
		if (s[i]=='-')
		{
			flag=false;
			break;
		}
	if (!flag)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n",ANS);
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int O;
	scanf("%d",&T);
	for (O=1;O<=T;O++)
	{
		ANS=0;
		printf("Case #%d: ",O);
		memset(s,0,sizeof(s));
		scanf("%s%d",s+1,&K);
		L=strlen(s+1);
		solve();
		check();
	}
}
