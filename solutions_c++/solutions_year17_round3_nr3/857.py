#include <bits/stdc++.h>
using namespace std;
double p[55];
int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int n,k;
		double u;
		cin>>n>>k>>u;
		for(int i=1;i<=n;i++){
			cin>>p[i];
		}
		int times =500;
		double left = 0,right = 1,mid,tmp;
		while(times--){
			mid = (left+right)/2;

			tmp = 0;
			for(int i=1;i<=n;i++){
				if(mid > p[i]) tmp += mid - p[i];
			}
			if(tmp > u) right = mid;
			else left = mid;
		}
		double ans = 1;

		for(int i=1;i<=n;i++){
			if(p[i]>mid) ans*=p[i];
			else ans*=mid;
		}
		printf("Case #%d: %.12f\n",t,ans);

	}
}