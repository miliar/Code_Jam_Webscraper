#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
typedef unsigned long long ll;
ll valid(ll n){
	ll prev = 9;
	while(n>0){
		ll current_digits = n%10;
		if(current_digits > prev)return false;
		prev = current_digits;
		n/=10;
	}
	return true;
}
ll change(ll n){
	vector<ll> values(25);
	while(!valid(n)){
		ll tmp = n;
		for(ll i = 0; tmp > 0; i++){
			values[i] = tmp%10;
			tmp/=10;
		}
		for(ll i = 0; i < 24; i++){
			if(values[i] < values[i+1]){
				values[i+1]--;
				for(ll j = 0; j <= i; j++){
					values[j] = 9;
				}
			}
		}
		ll ans = 0;
		ll current_times = 1;
		for(ll i = 0; i < 20; i++){
			ans += current_times*(values[i]);
			current_times*=10;
		}
		n = ans;
	}
	return n;
}
int main(){
	ll t;
	cin >> t;
	for(ll c = 1; c <= t; c++){
		ll n;
		cin >> n;
		ll loops = 1;
		n = change(n);
		cout << "Case #" << c << ": " << n <<endl;
	}
}