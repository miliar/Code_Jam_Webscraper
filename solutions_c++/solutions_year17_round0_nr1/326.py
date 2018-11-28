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

char s[100010];

void lemon()
{
	int K;
	scanf("%s%d",s+1, &K);
	int n=strlen(s+1);
	int ans=0;
	rep(i,1,n-K+1)
		if (s[i]=='-')
		{
			ans++;
			rep(j,i,i+K-1)
				if (s[j]=='+') s[j]='-'; else s[j]='+';
		}
	int flag=1;
	rep(i,1,n) if (s[i]=='-') flag=0;
	if (!flag) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);
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
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

