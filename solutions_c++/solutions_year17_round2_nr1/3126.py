#include <bits/stdc++.h>
using namespace std;

int main(){
	int t; cin>>t;
	for(int i=1;i<=t;++i){
		double d; int n; 
		cin>>d>>n;
		double k,s,ans=0.0;
		for(int j=0;j<n;++j){
			cin>>k>>s;
			double x=(d-k)/s;
			if(x>ans) ans=x;
		}
		ans=d/ans;
		printf("Case #%d: %.10lf\n",i,ans);
	}
	return 0;
}
