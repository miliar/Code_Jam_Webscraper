#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#define DO long double
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,n,c,m,x,y;
int ans,aaa;
int a[1010];
int b[1010];
int peo[1010];
int sum[1010];

bool check(int k) {
	for (int i=n;i;--i) {
		int tmp=min(peo[i],k);
		a[i]=peo[i]-tmp;
		b[i]=k-tmp;
	}
	REP(i,n) a[i]+=a[i-1];
	REP(i,n) b[i]+=b[i-1];
	REP(i,n) if (a[i]>b[i]) return false;
	aaa=a[n];
	return true;
}

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ", T_T);
		scanf("%d%d%d",&n,&c,&m);
		memset(peo,0,sizeof(peo));
		memset(sum,0,sizeof(sum));
		REP(i,m) {
			scanf("%d%d",&x,&y);
			peo[x]++;
			sum[y]++;
		}
		ans=0;
		REP(i,c)
			ans=max(ans,sum[i]-1);
		for (int i=1024;i;i>>=1)
			if (!check(ans+i))
				ans+=i;
		check(ans+1);
		printf("%d %d\n",ans+1, aaa);
	}
	return 0;
}