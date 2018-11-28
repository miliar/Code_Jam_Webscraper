#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#define DO long double
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

///////////////////ROYGBV
const char b[] = "#RYBGVO";
int T,n;
int a[11];
int aa[11];
int c[11];
int rest[11];
int ans[1010];

void work() {
	// only one color
	REP(k,3) {
		if (a[k]+a[k+3]==n && a[k]==a[k+3]) {
			REP(i,n/2) printf("%c%c",b[k],b[k+3]);
			puts("");
			return;
		}
	}
	if (a[1]<=a[4] && a[1]>0) {puts("IMPOSSIBLE");return;}
	if (a[2]<=a[5] && a[2]>0) {puts("IMPOSSIBLE");return;}
	if (a[3]<=a[6] && a[3]>0) {puts("IMPOSSIBLE");return;}
	c[1]=a[1]-a[4];rest[1]=a[4];
	c[2]=a[2]-a[5];rest[2]=a[5];
	c[3]=a[3]-a[6];rest[3]=a[6];
	if (c[1]>c[2]+c[3]) {puts("IMPOSSIBLE");return;}
	if (c[2]>c[1]+c[3]) {puts("IMPOSSIBLE");return;}
	if (c[3]>c[1]+c[2]) {puts("IMPOSSIBLE");return;}
	memset(ans,0,sizeof(ans));
	REP(i,c[1]) ans[i+i-1]=1;
	int last=0;
	// more first
	if (c[2]>c[3]) last=3;
	else last=2;
	int leave=c[1]+c[2]+c[3];
	// printf("%d %d %d\n",c[1],c[2],c[3]);
	for (int i=leave;i>0;) {
		if (ans[i]) {--i;continue;}
		int now=0;
		if (c[5-last]) now=5-last;
		else now=last;
		--c[now];
		ans[i]=now;
		last=now;
	}
	// REP(i,leave) printf("%d",ans[i]);puts("");
	REP(i,leave) {
		printf("%c",b[ans[i]]);
		int k=ans[i];
		if (rest[k]) {
			REP(j,rest[k]) printf("%c%c",b[k+3],b[k]);
			rest[k]=0;
		}
	}
	puts("");
}

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ", T_T);
		scanf("%d",&n);
		REP(i,6) scanf("%d",&aa[i]);
		a[1]=aa[1];
		a[2]=aa[3];
		a[3]=aa[5];
		a[4]=aa[4];
		a[5]=aa[6];
		a[6]=aa[2];
		work();
	}

	return 0;
}