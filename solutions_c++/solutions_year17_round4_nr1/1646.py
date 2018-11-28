#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

#define MAXN 1000

void solve() {
	int x,n,p;
	int a[5];
	for (int i=0;i<5;i++) a[i]=0;
	scanf("%d%d",&n,&p);
	for (int i=0;i<n;i++) {
		scanf("%d",&x);
		a[x%p]++;
	}
	int ans = a[0];
	if (p==2) {
		ans+=(a[1]+1)/2;
	}
	if (p==3) {
		int t = min(a[1],a[2]);
		ans+=t;
		t = max(a[1],a[2]) - t;
		ans+=(t+2)/3;
	}
	printf("%d\n",ans);
}

int main() {
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		solve();
	}

	return 0;
}