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

int n,p,a[500],cnt[5];


int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\r2\\a\\A-small-attempt0.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\r2\\a\\mysmalloutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%d%d",&n,&p);
		clr(cnt,0);
		rep(i,1,n)
		{
			scanf("%d",&a[i]);
			cnt[a[i]%p]++;
		}
		int ans=cnt[0];
		if(p==2)
		{
			ans+=(cnt[1]+1)/2;
		}
		else if(p==3)
		{
			while(cnt[1] && cnt[2])
			{
				ans++;
				cnt[1]--;
				cnt[2]--;
			}
			ans+=(cnt[1]+2)/3 + (cnt[2]+2)/3;
		}
		else if(p==4)
		{
			while(cnt[1] && cnt[3])
			{
				ans++;
				cnt[1]--;
				cnt[3]--;
			}
			while(cnt[2]>1)
			{
				ans++;
				cnt[2]-=2;
			}
			while(cnt[1]>3)
			{
				ans++;
				cnt[1]-=4;
			}
			while(cnt[3]>3)
			{
				ans++;
				cnt[3]-=4;
			}
			int t=cnt[1]>0?1:3;
			while(cnt[t]>1 && cnt[2])
			{
				ans++;
				cnt[t]-=2;
				cnt[2]--;
			}
			if(cnt[0]+cnt[1]+cnt[2])ans++;
		}
		
		printf("Case #%d: %d\n",ii,ans);
	}
	
	
	return 0;
}
