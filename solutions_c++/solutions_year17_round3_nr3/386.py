#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

#define MAXN 55

bool cmp(double a,double b) {
	return a>b;
}



void solve() {
	double p[MAXN],u;
	int n,k;
	scanf("%d%d",&n,&k);
	scanf("%lf",&u);
	double sum_p = 0;
	for (int i=0;i<n;i++) {
		scanf("%lf",&p[i]);
		sum_p += p[i];
	}
	sort(p,p+n,cmp);
	double ep,ans=1;
	for (int i=0;i<n;i++) {
		ep = (sum_p+u)/(n-i);
		if (ep>=p[i]) {
			for (int j=i;j<n;j++)
				ans *= ep;
			printf("%.9lf\n",ans);
			return;
		}
		sum_p -= p[i];
		ans *= p[i];
	}
	printf("%.9lf\n",ans);

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