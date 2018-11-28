#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;
typedef long long LL;
typedef long double LD;
vector<pair<LD, LD> > v;

int main(){
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int T=1;  T<=t; ++T){
		LL d, n;
		cin>>d>>n;
		for(int i=0; i<n; i++){
			LD a, b;
			cin>>a>>b;
			v.push_back(make_pair(a, b));
		}
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		LD time=0;
		for(auto it=v.begin(); it!=v.end(); ++it){
			time = max(time, ((d-it->first)/it->second));
		}
		std::cout << std::fixed;
		cout<<"Case #"<<T<<": "<<setprecision(6)<<d/time<<"\n";	
		v.clear();	
	}
	return 0;
}
