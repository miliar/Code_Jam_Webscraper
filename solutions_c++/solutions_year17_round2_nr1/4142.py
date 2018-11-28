#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

int main(){
	int t;
	cin>>t;
	int k=0;
	while(t--){
		k++;
		double d;
		lli n;
		cin>>d>>n;
		pair<double,double> a[n];
		pair<double,double> p;
		for(lli i=0;i<n;i++){
			cin>>p.first>>p.second;
			a[i]=p;
		}
		sort(a,a+n);
		double ans=0;
		if(n==2){
			if(a[0].second<=a[1].second){
				ans=(d-a[0].first)/(a[0].second);
				ans=(d/ans);
			}else{
				if((a[1].first-a[0].first)/(a[0].second-a[1].second) > (d-a[1].first)/(a[1].second)){
					ans=(d-a[0].first)/(a[0].second);
					ans=(d/ans);
				}else{
					ans=(a[1].first-a[0].first)/(a[0].second-a[1].second);
					ans+=(d-(a[0].second*(ans) + a[0].first))/(a[1].second);
					ans=d/ans;
				}
			}
		}else{
			ans=(d-a[0].first)/(a[0].second);
			ans=(d/ans);
		}
		cout<<setprecision(6)<<fixed;
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}