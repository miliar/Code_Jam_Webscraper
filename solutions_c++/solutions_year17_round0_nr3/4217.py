#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

typedef long long int ll;

//#define DEBUG 1

using namespace std;

template <class Type>
void output(const vector<Type>& v) {
	cout << "Print: ";
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

string calMlr(ll x) {
	#ifdef DEBUG
	cout << "calMlr : " << x << endl;
	#endif
	
	ll s = 0;
	ll e = x - 1;
	ll mid = e / 2;
	ll ls = mid - s;
	ll rs = e - mid;
	return to_string(max(ls, rs)) + " " + to_string(min(ls, rs));
}

string solve(ll n, ll k) {
	priority_queue<ll> q;
	q.push(n);
	for(int i = 0; i < k -1; i++) {
		ll x = q.top();
		q.pop();
		
		#ifdef DEBUG
		cout << "top : " << x << endl;
		#endif
		
		if (x == 1) {
			q.push(x / 2);
		} else {
			ll l = x / 2 - (1 - (x % 2));
			ll r = x / 2;
			q.push(l), q.push(r);
			#ifdef DEBUG
			cout << "push : " << l << endl;
			cout << "push : " << r << endl;
			#endif
		}
	}
	return calMlr(q.top());
}

int main() {
	int T;
	cin >> T;
	for(int cas=1; cas <=T; cas++) {
		string pancakes;
		ll n, k;
		cin >> n >> k;
		cout << "Case #" << cas << ": " << solve(n, k) << endl;
	}
	return 0;
}
