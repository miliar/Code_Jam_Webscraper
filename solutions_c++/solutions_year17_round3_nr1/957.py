#include<bits/stdc++.h>
using namespace std;
struct P{
	long long R,H;
}a[1000],b[1000];
bool comp1(P x,P y){
	return x.R!=y.R?x.R>y.R:x.H>y.H;
}
bool comp2(P x,P y){
	return x.R*x.H!=y.R*y.H?x.R*x.H>y.R*y.H:x.R>y.R;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	long double pi=3.14159265358979;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int n,k;
		long double ans=0;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lld%lld",&a[i].R,&a[i].H);
		}
		sort(a,a+n,comp1);
		for(int i=0;i<=n-k;i++){
			long double cnt=pi*a[i].R*a[i].R;
			for(int j=i;j<n;j++){b[j]=a[j];}
			sort(b+i+1,b+n,comp2);
			cnt+=2*pi*a[i].R*a[i].H;
			for(int j=i+1;j<i+k;j++){
				cnt+=2*pi*b[j].R*b[j].H;
			}
			if(ans<cnt)ans=cnt;
		}
		printf("Case #%d: %10Lf\n",i+1,ans);
	}
}
