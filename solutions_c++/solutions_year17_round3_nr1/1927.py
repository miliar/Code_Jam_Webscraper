#include"bits/stdc++.h"
using namespace std;
int main(){
	ifstream in("A-large.in.txt");
	ofstream out("output.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;++i){
		int n,k;
		in>>n>>k;
		vector<pair<long double,long double>> x;
		long double temp1,temp2,pi=3.14159265358979323846264338327;
		for(int j=0;j!=n;++j){
			in>>temp1>>temp2;
			x.push_back({temp1,temp2});
		}
		sort(x.rbegin(),x.rend());
		long double ans=0;
		for(int i=0;i+k-1!=n;++i){
			long double cur=x[i].first*x[i].first+2*x[i].first*x[i].second;
			vector<long double> y;
			for(int j=i+1;j!=n;++j)
				y.push_back(x[j].first*2*x[j].second);
			sort(y.rbegin(),y.rend());
			for(int j=0;j!=k-1;++j)
				cur+=y[j];
			ans=max(cur,ans);
		}
		out<<"Case #"<<i<<": "<<setprecision(25)<<pi*ans<<endl;
	}
}



