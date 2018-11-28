#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

#define MAXN 1000

struct node{
	long long r,h;
	long long c;
} a[MAXN];

bool cmp(node a,node b) {
	return a.c>b.c;
}

int n,k;

void solve() {
	scanf("%d%d",&n,&k);
	for (int i=0;i<n;i++) {
		scanf("%lld%lld",&a[i].r,&a[i].h);
		a[i].c = 2*a[i].r*a[i].h;
	}
	sort(a,a+n,cmp);
	long long tmp,ans=0;
	int cnt;
	for (int i=0;i<n;i++) {
		tmp = a[i].r*a[i].r + a[i].c;
		cnt = 0;
		for (int j=0;j<n;j++) {
			if (cnt==k-1) break;
			if (i!=j) {
				tmp += a[j].c;
				cnt++;
			}
		}
		if (tmp>ans) ans = tmp;
	}
	double dans = ans*M_PI;
	printf("%.9lf\n",dans);
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