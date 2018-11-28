#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const int maxn=55;
const double eps=1e-6;
int T,n,k,key;
double last,a[maxn];
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int u=1; u<=T; u++) {
		scanf("%d%d",&n,&k);
		scanf("%lf",&last);
		for (int i=1; i<=n; i++) scanf("%lf",&a[i]);
		sort(a+1,a+n+1);
		//for (int i=1; i<=n; i++) printf("%.6lf\n",a[i]);
		a[n+1]=1.00;
		for (int i=2; i<=n+1; i++) {
			double now=a[i]-a[i-1];
			if (fabs(a[i]-a[i-1])<eps) continue;
			//printf("%.15lf\n",now*(double)(i-1));
			//printf("%.15lf\n",last);
			if (now*(double)(i-1)<=last || fabs(last-now*(double)(i-1))<eps) {
				fill(a+1,a+i,a[i]),last-=(now*(double)(i-1));
				//for (int i=1; i<=n; i++) printf("%.6lf\n",a[i]);printf("%.6lf\n",last);
				//printf("\n");
			}
			else {key=i; break;}
		}
		if (last>eps) {
			double tba=last/((key-1)*1.00);
			for (int i=1; i<key; i++) a[i]+=tba;
		}
		double ans=1.00;
		for (int i=1; i<=n; i++) ans*=(a[i]*1.00);
		ans=min(ans,1.00);
		//for (int i=1; i<=n; i++) printf("%.6lf\n",a[i]);
		printf("Case #%d: %.6lf\n",u,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
