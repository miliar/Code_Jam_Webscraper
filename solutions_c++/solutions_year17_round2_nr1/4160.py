#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for (int cs=1; cs<=t; cs++){
		cout<<"Case #"<<cs<<": ";

		double d, n;
		cin>>d>>n;
		vector<double> k;
		vector<double> s;
		for (int i=0; i<n; i++){
			double ki, si;
			cin>>ki>>si;
			k.push_back(ki);
			s.push_back(si);
		}double ans;
		if(n==1)
		ans= d/((d-k[0])/s[0]);
		if(n>1){
		//cout<<max(((d-k[0])/s[0]), ((d-k[1])/s[1]));
		ans = d/(max(((d-k[0])/s[0]), ((d-k[1])/s[1])));
	}
		cout<<fixed;	
		cout<<setprecision(6)<<ans;

		cout<<endl;
	}
	return 0;
}