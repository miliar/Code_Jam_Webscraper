#include <bits/stdc++.h>
using namespace std;

int t,n,k;
double u,arr[55];

int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d%d",&n,&k);
		scanf("%lf",&u);
		for(int i=0;i<n;i++) scanf("%lf",&arr[i]);
		sort(arr,arr+n);
		int idx=-1;
		for(int i=1;i<n;i++){
			if(u<i*(arr[i]-arr[i-1])) {idx=i;break;}
			u-=i*(arr[i]-arr[i-1]);
			for(int j=0;j<i;j++) arr[j]=arr[i];
		}
		if(idx==-1) idx=n;
		for(int i=0;i<idx;i++){
			arr[i]+=(u/idx);
		}
		double ans=1;
		for(int i=0;i<n;i++) ans*=arr[i];
		printf("Case #%d: %lf\n",tc,ans);
	}
}
