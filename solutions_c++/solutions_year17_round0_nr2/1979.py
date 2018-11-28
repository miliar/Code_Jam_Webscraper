#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<utility>
#include<map>
#include<set>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define REP(i,a,b) for(int i=a; i<=b; ++i)
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define MP make_pair
#define sf scanf
#define pf printf
typedef long long LL;
typedef pair<int,int> pii;

int main()
{
	int T;
	LL n, ans, tmp;
	sf("%d", &T);
	REP(t,1,T)
	{
		sf("%lld", &n);
		ans = 0;
		for(int i=1; i<=9; ++i)
		{
			tmp = 1;
			while(ans+tmp <= n)
			{
				ans += tmp;
				tmp *= 10;
			}
		}
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}
