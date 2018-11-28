#include <iostream>
#include <utility>
#include <vector>
#include <iomanip>
using namespace std;
int main() {
	long long t;
	cin>>t;
	for(long long cas=1;cas<=t;cas++) {
		long long d,n;
		cin>>d>>n;
		long long k,s;
		vector< pair<long long,long long>  >horses;
		for(long long i=0;i<n;i++) {
			long long k,s;
			cin>>k>>s;
			horses.push_back(make_pair(k,s));
		}
		long long current=0;
		for(long long i=1;i<n;i++) {
			long long mk=horses[current].first;
			long long ms=horses[current].second;
			long long ck=horses[i].first;
			long long cs=horses[i].second;
			
			if((d-ck)*ms>(d-mk)*cs) {
				current=i;
			}	
		}
		double ans=d*horses[current].second;
		ans = ans / (d-horses[current].first);
		cout<<"Case #"<<cas<<": "<<fixed<<setprecision(6)<<ans<<endl;
	}
	return 0;
}
