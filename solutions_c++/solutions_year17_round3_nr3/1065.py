#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	ll t;
	cin >> t;
	std::cout.precision(7);
	for(int c = 1; c <= t; c++){
		ll n,k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> cores(n);
		for(int i = 0; i < n; i++){
			cin >> cores[i];
		}
		sort(cores.begin(),cores.end());
		if(k < n)cores.erase(cores.begin(), cores.begin() + n-k);
		map<double,ll> values;
		for(int i = 0; i < cores.size(); i++){
			values[cores[i]]++;
		}
		while(u > 0){
			pair<double,ll> lowest = *values.begin();
			if(lowest.first == 1.0)break;
			pair<double,ll> next;
			values.erase(values.begin());
			if(values.size() > 0){
				next = (*values.begin());
			}
			else next = {1.0,1};
			if((next.first - lowest.first)*lowest.second <= u){
				u-=(next.first - lowest.first)*lowest.second;
				values[next.first]+=lowest.second;
			}
			else{
				values[lowest.first + (u/lowest.second)] = lowest.second;
				u = 0;
			}
		}
		double ans = 1.0;
		for(pair<double,ll> current: values){
			for(int i = 0; i < current.second; i++){
				ans*=current.first;
			}
		}
		cout << "Case #" << c << ": " << fixed << ans << endl;
	}
}