#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

int r,c;
char cake[100][100];

void lemon()
{
	scanf("%d%d",&r,&c);
	rep(i,1,r) scanf("%s",cake[i]+1);
	int first=1;
	rep(i,1,r)
	{
		int flag=0; char color;
		rep(j,1,c)
			if (cake[i][j]!='?')
			{
				flag=1; color=cake[i][j]; break;
			}
		if (flag==0 && first) continue;
		if (flag==0)
		{
			rep(j,1,c) cake[i][j]=cake[i-1][j];
			continue;
		}
		first=0;
		rep(j,1,c)
		{
			if (cake[i][j]!='?') color=cake[i][j];
			cake[i][j]=color;
		}
	}
	repd(i,r-1,1)
		rep(j,1,c)
			if (cake[i][j]=='?')
				cake[i][j]=cake[i+1][j];
	
	rep(i,1,r) printf("%s\n",cake[i]+1);
			
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("A.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d:\n",i);
		lemon();
	}
	return 0;
}

