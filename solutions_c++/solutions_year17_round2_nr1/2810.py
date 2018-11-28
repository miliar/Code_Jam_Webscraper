#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		ll d;
		int n;
		cin>>d;
		cin>>n;
		double ans=90000000000000000.000000;
		for(int i=0;i<n;i++){
			ll k,s;
			cin>>k>>s;
			ll val=d-k;
			double tmp=((double)val/s);
			double vt=((double)d/tmp);
			ans=min(ans,vt);
			}
		cout<<"Case #"<<t<<": ";
		cout<<setprecision(6)<<fixed<<ans<<endl;
		}
	return 0;
	}
