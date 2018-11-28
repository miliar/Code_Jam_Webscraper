#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LL long long
#define min(a,b) ((a<b)?a:b)
#define max(a,b) ((a>b)?a:b)
#define fo(i,j,k) for(LL i=j;i<=k;i++)
#define fd(i,j,k) for(LL i=j;i>=k;i--)
using namespace std;
LL const maxn=3*1e4,inf=1e9;
LL t,n,K;long double f[1009],pi=3.141592653589793238462643383;
struct rec{
	LL r,h;
};
rec a[1009];
bool cmp(rec x,rec y){
	return x.r<y.r;
}
int main(){
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%lld",&t);
	fo(cas,1,t){
		scanf("%lld%lld",&n,&K);
		fo(i,1,n)scanf("%lld%lld",&a[i].r,&a[i].h);
		sort(a+1,a+n+1,cmp);
		fo(i,0,K)f[i]=0;double ans=0;
		fo(i,1,n){
			ans=max(ans,f[K-1]+2*pi*a[i].r*a[i].h+pi*a[i].r*a[i].r);
			fd(j,K,1)f[j]=max(f[j],f[j-1]+2*pi*a[i].r*a[i].h);
		}
		printf("Case #%lld: %.9lf\n",cas,ans);
	}
	
	return 0;
}
