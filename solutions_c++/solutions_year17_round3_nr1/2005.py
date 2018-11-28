#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n;
vector<pair<ll,ll> > pancakes;
map<pair<ll,ll>,double> dp_table;
const double PI = 3.14159265359;
inline double area_difference(ll r1, ll r2){
	return (r1*r1*PI) - r2*r2*PI;
}
double dp(ll current_index, ll remaining){
	if(remaining == 0)return 0;
	double ans = 0;
	if(dp_table.count({current_index,remaining}) > 0)return dp_table[{current_index,remaining}];
	for(int i = current_index+1; i <= n - remaining; i++){
		double tmp = dp(i,remaining-1) + area_difference(pancakes[current_index].first,pancakes[i].first) + (2*PI*pancakes[i].first*pancakes[i].second);
		if(remaining == 1)tmp += area_difference(pancakes[i].first,0);
		ans = max(ans,tmp);
	}
	return ans;
}
int main(){
	ll t;
	cin >> t;
	std::cout.precision(10);
	for(int c = 1; c <= t; c++){
		ll k;
		cin >> n >> k;
		pancakes.resize(n);
		for(int i = 0; i < n; i++){
			cin >> pancakes[i].first >> pancakes[i].second;
		}
		sort(pancakes.rbegin(),pancakes.rend());
		double ans = 0;
		for(int i = 0; i <= n-k; i++){
			double tmp;
			if(k == 1)tmp = (2*PI*pancakes[i].first*pancakes[i].second) + area_difference(pancakes[i].first,0);
			else tmp = dp(i,k-1) + (2*PI*pancakes[i].first*pancakes[i].second);
			ans = max(tmp,ans);
		}
		cout << "Case #" << c << ": "  << fixed << ans << endl;
	}
	return 0;
}