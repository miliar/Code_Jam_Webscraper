#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007
const int maxn=1010;
char s[maxn];


int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\qround\\a\\A-large.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\qround\\a\\mylargeoutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		int k;
		scanf("%s%d",s+1,&k);
		printf("Case #%d: ",ii);
		int n=strlen(s+1);
		rep(i,1,n)
		{
			s[i]= s[i]=='+'?1:0;
		}
		bool ok=1;
		int ans=0;
		rep(i,1,n)
		{
			if(i<=n-k+1)
			{
				if(s[i]==0)
				{
					ans++;
					rep(j,i,i+k-1)s[j]^=1;
				}
			}
			else
			{
				if(s[i]==0)ok=0;
			}
		}
		if(!ok)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	
	
	return 0;
}
