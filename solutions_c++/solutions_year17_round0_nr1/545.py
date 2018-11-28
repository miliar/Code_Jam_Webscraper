#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

const int maxn = 1010;

char st[maxn];

void init()
{
	int m,s=0;
	scanf("%s%d",st+1,&m);
	int n=strlen(st+1);
	REP(i,1,n-m+1)
		if(st[i]=='-')
		{
			REP(j,0,m-1)
				if(st[i+j]=='-') st[i+j]='+';
				else st[i+j]='-';
			++s;
		}
	REP(i,1,n)
		if(st[i]=='-')
		{
			puts("IMPOSSIBLE");
			return;
		}
	printf("%d\n",s);
}

void solve()
{
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	REP(i,1,T)
	{
		printf("Case #%d: ",i);
	init();
	solve();
	}
	
	return 0;
}
