#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second
typedef long long LL;
typedef pair<LL,LL> PI;
double pi = acos(-1);

int n,k;
PI a[1100];
LL b[1100];

int main()
{
	int T,t=0;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++) scanf("%lld%lld",&a[i].x,&a[i].y);
		sort(a,a+n);
		reverse(a,a+n);
		double ans=0;
		for (int i=0;i<n;i++) {
			if (n-i<k) break;
			double tot=a[i].x*a[i].x*pi+a[i].x*a[i].y*2*pi;
			for (int j=i+1;j<n;j++) b[j-i-1]=a[j].x*a[j].y;
			sort(b,b+n-i-1);
			reverse(b,b+n-i-1);
			for (int j=0;j<k-1;j++)
				tot+=b[j]*2*pi;
			if (tot > ans) ans=tot;
		}
		printf("Case #%d: %.9lf\n",++t,ans);
	}
}
