#include <bits/stdc++.h>
using namespace std;
#define maxn 1020
typedef long long LL;
typedef pair<double, double> pdd;
pdd h[maxn];
int n;
double m;

bool judge(double limit){
	for (int i=1;i<=n;i++)
		if ((limit*h[i].first)<m*(limit-h[i].second)) return 0;
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%lf%d",&m,&n);
		for (int i=1;i<=n;i++)
			scanf("%lf%lf",&h[i].first, &h[i].second);
		//sort(h+1, h+n+1);
		double l=0, r=1e13, eps=1e-7, ans;
		for (int i=1;i<=10000;i++){
			double mid=(l+r)/2.0;
			if (judge(mid)){
				l=mid+eps;
				ans=mid;
			}
			else{
				r=mid-eps;
			}
		}
		printf("Case #%d: %.6f\n", o, ans);
	}
	return 0;
}