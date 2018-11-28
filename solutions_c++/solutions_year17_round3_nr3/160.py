#include <bits/stdc++.h>

using namespace std;
int n;
double arr[219],u;
bool check(double t){
	double sum=0;
	for(int i=0;i<n;i++){
		if(t-arr[i]<0)continue;
		sum+=(t-arr[i]);
	}
	if(sum<=u)return true;
	else return false;
}
int main(){
	int tc,tci=1;cin>>tc;
	while(tc-->0){
		int k;cin>>n>>k;
		cin>>u;
		for(int i=0;i<n;i++)cin>>arr[i];
		double l=0,r=1,ans=1;
		while(r-l>1e-9){
			double mid=(l+r)/2;
			if(check(mid))l=mid;
			else r=mid;
		}
		for(int i=0;i<n;i++)
			if(arr[i]<l)ans*=l;
			else ans*=arr[i];
		cout<<"Case #"<<tci++<<": "<<fixed<<setprecision(6)<<ans<<endl;
	}
}
