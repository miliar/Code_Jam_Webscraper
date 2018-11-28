#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
int main(){
	ll t;
	cin >> t;
	for(ll c = 1; c <= t; c++){
		map<ll,ll> values;
		ll n,k;
		cin >> n >> k;
		set<ll> s;
		s.insert(n);
		values[n] = 1;
		ll l,r;
		ll iterations = 0;
		while(k > iterations){
			ll current = *s.rbegin();
			s.erase(*s.rbegin());
			l = (current/2);
			r = current-(current/2) - 1;
			iterations += values[current];
			values[l] += values[current];
			values[r] += values[current];
			s.insert(l);
			s.insert(r);
		}
		cout << "Case #" << c << ": " << max(abs(r),abs(l)) << ' ' << min(abs(r),abs(l)) << endl;
	}
	return 0;
}