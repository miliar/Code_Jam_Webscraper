#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

int main(){
	int t;
	cin>>t;
	int z=0;
	while(t--){
		z++;
		lli n;
		double k;
		lli u;
		cin>>n>>u>>k;
		double a[n];
		for(lli i=0;i<n;i++){
			cin>>a[i];
		}
		sort(a,a+n);
		lli i=0;
		while(k>0 && i<n-1){
			double x=a[i+1]-a[i];
			x=min(x*(i+1),k);
			x=x/(i+1);
			for(lli j=0;j<=i;j++){
				a[j]=min(1.0,a[j]+x);
			}
			k=k-(x*(i+1));
			i++;
		}
		if(k!=0){
			double x=k/n;
			for(lli j=0;j<n;j++){
				a[j]=min(1.0,a[j]+x);
			}
		}
		double ans=1;
		for(i=0;i<n;i++){
			ans=ans*a[i];
		}
		cout<<setprecision(6)<<fixed;
		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}