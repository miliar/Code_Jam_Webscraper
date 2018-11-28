#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 53
double a[maxn];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		int k,n;
		double u;
		scanf("%d%d",&k,&n);
		scanf("%lf",&u);
		for (int i=1;i<=n;i++) {
			scanf("%lf",a+i);
		}
		sort(a+1,a+1+n);
		a[n+1]=1;
		for (int i=1;i<=n;i++) {
			double tmp=(a[i+1]-a[i]);
			if (tmp*i>u) tmp=u/i;
			u-=tmp*i;
			for (int j=1;j<=i;j++) a[j]+=tmp;
		}
		double ans=1;
		for (int i=1;i<=n;i++) ans*=a[i];
		printf("Case #%d: %.8lf\n",_,ans);
	}
	return 0;
}
