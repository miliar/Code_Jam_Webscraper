#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
struct data{
	int r,h;
	double s;
}a[2101];
double pi,ans,tmp,b[2101];
int i,j,k,n,m,tests,tc;
bool cmp(data a,data b){
	return a.r>b.r||a.r==b.r&&a.s>b.s;
}
bool cmp1(double a,double b){
	return a>b;
}
int main(){
	pi=acos(-1);
	for (scanf("%d",&tests),tc=1;tc<=tests;tc++){
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++){
			scanf("%d%d",&a[i].r,&a[i].h);a[i].s=pi*2*a[i].r*a[i].h;
		}
		sort(a+1,a+1+n,cmp);ans=0;
		for (i=1;i<=n;i++){
			for (j=i+1,k=0;j<=n;j++) b[++k]=a[j].s;
			if (k<m-1) break;
			sort(b+1,b+k+1,cmp1);
			for (tmp=a[i].s+pi*a[i].r*a[i].r,j=1;j<m;j++) tmp+=b[j];
			ans=max(ans,tmp);
		}
		printf("Case #%d: %.9f\n",tc,ans);
	}
	return 0;
}
