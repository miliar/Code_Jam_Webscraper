/*input

*/
#include <bits/stdc++.h>
using namespace std;
pair< double,double >  a[1005];
int main(){
	ios_base::sync_with_stdio(0);
	long long int tc=1,T;
	for(cin>>T;tc<=T;++tc){
		double d,n,time=0;
		cin>>d>>n;
		for(int i=0;i<n;cin>>a[i].first>>a[i].second,++i);
		for(int i=0;i<n;++i){
			time=max(time, (d-a[i].first)/a[i].second);
		}
		cout<<"Case #"<<tc<<": ";
		cout<<fixed<<setprecision(6)<<d/time<<'\n';
	}
}