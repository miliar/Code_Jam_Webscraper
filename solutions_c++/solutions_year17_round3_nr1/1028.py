#include <bits/stdc++.h>
using namespace std;
const double pi = acos(-1);
struct cake{
	double r,h;
	bool operator < (const cake &XD) const{
		return r > XD.r;
	}
}a[1010];

struct egg{
	double r,h;
	bool operator < (const egg &XD) const{
		return r*h > XD.r*XD.h;
	}
}b[1010];
int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++){
			cin>>a[i].r>>a[i].h;
		}
		sort(a+1,a+n+1);
		double ans = 0;
		for(int i=1;i<=n-k+1;i++){
			for(int j=i;j<=n;j++){
				b[j].r=a[j].r;
				b[j].h=a[j].h;
			}
			sort(b+i+1,b+n+1);
			double tmp = 0;
			for(int j=0;j<k;j++){
				tmp+=b[i+j].r*b[i+j].h*2*pi;
			}
			tmp+=pi*b[i].r*b[i].r;
			if(tmp>ans) ans = tmp;
		}
		printf("Case #%d: %.12f\n",t,ans);

	}
}