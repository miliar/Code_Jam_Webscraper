#include<cstdio>
#include<algorithm>
using namespace std;
const double pi=3.141592653589793238;
struct data{
	long long r,h,val;
}a[1010];
long long T,n,k;
bool cmp(const data &x,const data &y) {
	return x.val<y.val;
}
bool cmp1(const data &x,const data &y) {
	return (x.h*x.r)>(y.h*y.r);
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout); 
	scanf("%lld",&T);
	for (long long u=1; u<=T; u++) {
		scanf("%lld%lld",&n,&k);
		double ans=0.0;
		for (long long i=1; i<=n; i++) scanf("%lld%lld",&a[i].r,&a[i].h),a[i].val=a[i].r*a[i].r;
		sort(a+1,a+n+1,cmp);
		for (long long i=k; i<=n; i++) {
			double now=0.0;
			now+=pi*a[i].val;
			now+=a[i].r*2*pi*a[i].h;
			sort(a+1,a+i,cmp1);
			for (long long j=1; j<k; j++) now+=a[j].h*2*a[j].r*pi;
			ans=max(ans,now);
			sort(a+1,a+i,cmp);
		}
		printf("Case #%lld: %.9lf\n",u,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
