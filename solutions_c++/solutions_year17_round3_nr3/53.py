#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
double w,a[101],ans,tmp;
int tests,tc,i,j,k,n,m;
int main(){
	for (scanf("%d",&tests),tc=1;tc<=tests;tc++){
		scanf("%d%d%lf",&n,&m,&w);
		for (i=1;i<=n;i++) scanf("%lf",&a[i]);
		sort(a+1,a+1+n);
		for (i=1;i<n;i++){
			while (i<n&&a[i+1]==a[i]) i++;
			if (i==n||w<i*(a[i+1]-a[i])) break;
			w-=i*(a[i+1]-a[i]);
		}
		tmp=a[i]+w/i;
		for (ans=1,j=1;j<=i;j++) ans*=tmp;
		for (j=i+1;j<=n;j++) ans*=a[j];
		printf("Case #%d: %.9f\n",tc,ans);
	}
	return 0;
}
