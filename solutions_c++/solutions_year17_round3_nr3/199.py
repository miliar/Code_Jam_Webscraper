#include <bits/stdc++.h>
using namespace std;

double a[50];

int main(){
	double u,ans;
	int t,tt,n,m,i,j,k;
	cin >> t;
	for(tt=1;tt<=t;tt++){
		cin >> n >> k >> u;
		for(i=0;i<n;i++)
			cin >> a[i];
		a[n]=1;n++;
		sort(a,a+n);
		ans=1;
		for(i=1;i<n;i++){
			if(i*(a[i]-a[i-1])<=u){
				u-=i*(a[i]-a[i-1]);
			}
			else{
				ans=pow(a[i-1]+u/i,i);
				for(;i<n;i++)
					ans*=a[i];
			}
		}
		printf("Case #%d: %.8lf\n",tt,ans);
	}
}
